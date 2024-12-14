import time

from picamera2 import Picamera2


picam = Picamera2()

sconfig = picam.create_still_configuration()
picam.configure(sconfig)
print('Say "cheese!"')
picam.start_preview()
picam.start()
time.sleep(1)
picam.capture_file("image.jpg")
picam.stop_preview()
picam.stop()
print('Image captured')

# same as above, using convenience method
print('Say "cheese!"')
picam.start_and_capture_file()
print('Image captured')
