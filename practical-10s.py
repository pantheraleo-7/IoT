# pip install adafruit-circuitpython-fingerprint
import adafruit_fingerprint as fp
import serial


usb = serial.Serial("/dev/ttyUSB0", baudrate=57600, timeout=1)
sensor = fp.Adafruit_Fingerprint(usb)


def search():
    print("Place finger on the sensor...")
    return_code = sensor.get_image()
    while return_code == fp.NOFINGER:
        return_code = sensor.get_image()

    sensor.image_2_tz()

    return_code = sensor.finger_fast_search()
    if return_code == fp.OK:
        print(f"Detected #{sensor.finger_id} with confidence {sensor.confidence}")
    if return_code == fp.NOTFOUND:
        print("Fingerprint not found")


def enroll(id):
    for i in range(2):
        print(f"Place finger on the sensor{" again"*i}...")
        return_code = sensor.get_image()
        while return_code == fp.NOFINGER:
            return_code = sensor.get_image()

        sensor.image_2_tz(i+1)

    sensor.create_model()

    return_code = sensor.store_model(id)
    if return_code == fp.OK:
        print(f"Model stored at #{id}")


id = int(input(f"Enter ID [0-{sensor.library_size}): "))
enroll(id)
search()
