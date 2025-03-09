# pip install adafruit-circuitpython-pn532
import board
from adafruit_pn532 import adafruit_pn532 as pn532
from adafruit_pn532.i2c import PN532_I2C


ADDR = 0x24

i2c = board.I2C()
nfc = PN532_I2C(i2c, ADDR)

ic, ver, rev, support = nfc.firmware_version
print(f"Found PN532 with firmware version: {ver}.{rev}")

nfc.SAM_configuration()


def read(block=4, key=bytes.fromhex("ffffffffffff"), timeout=5.0):
    uid = nfc.read_passive_target(timeout=timeout)
    authenticated = nfc.mifare_classic_authenticate_block(uid, block, pn532.MIFARE_CMD_AUTH_A, key)
    if authenticated:
        return nfc.mifare_classic_read_block(block)

    raise PermissionError(f"Authentication failed: detected {uid = }")


def write(data, block=4, key=bytes.fromhex("ffffffffffff"), timeout=5.0):
    uid = nfc.read_passive_target(timeout=timeout)
    authenticated = nfc.mifare_classic_authenticate_block(uid, block, pn532.MIFARE_CMD_AUTH_B, key)
    if authenticated:
        data = data.encode().ljust(16)[:16]
        return nfc.mifare_classic_write_block(block, data)

    raise PermissionError(f"Authentication failed: detected {uid = }")


print("Writing to block 4...", end=" ", flush=True)
if write("Hello, world!"):
    print("successful")
    print("Reading from block 4...", end=" ", flush=True)
    if (data:=read()) is not None:
        print("successful")
        print(f"{data = }")
    else:
        print("failed")
else:
    print("failed")
