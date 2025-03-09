import time

from picamera2 import Picamera2


picam = Picamera2()

sconfig = picam.create_still_configuration()
picam.configure(sconfig)

picam.start_preview(True)
picam.start()

print("Taking image...")
time.sleep(1)
picam.capture_file("image.jpg")
print("Image captured")

picam.stop_preview()
picam.stop()

# using convenience method
# print("Taking image...")
# picam.start_and_capture_file()
# print("Image captured")

picam.close()
