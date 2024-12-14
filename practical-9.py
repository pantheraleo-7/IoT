import time
# pip install mfrc522
from mfrc522 import SimpleMFRC522
from RPi import GPIO


rfid = SimpleMFRC522()


def write():
    try:
        while True:
            data = input("Enter the data to write: ")
            print("Write started, place a card")
            rfid.write(data)
            print("Write complete.")
            time.sleep(5)
    except KeyboardInterrupt:
        print("Write stopped.")
    finally:
        GPIO.cleanup()


def read():
    try:
        while True:
            print("Read started, place a card.")
            id, text = rfid.read()
            print(f"{id =}\n{text =}")
            time.sleep(5)
    except KeyboardInterrupt:
        print("Read stopped.")
    finally:
        GPIO.cleanup()
