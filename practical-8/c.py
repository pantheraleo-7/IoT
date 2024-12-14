import time

from picamera2 import Picamera2


picam = Picamera2()

pconfig = picam.create_preview_configuration()
sconfig = picam.create_still_configuration()
picam.configure(pconfig)
print("Starting camera..")
picam.start_preview()
picam.start()
print('Say "cheese!"')
picam.switch_mode(sconfig)
time.sleep(1)
img1 = picam.capture_image()
print('Image 1 captured.')
picam.switch_mode(pconfig)
time.sleep(5)
print('Say "cheese!"')
picam.switch_mode(sconfig)
time.sleep(1)
img2 = picam.capture_image()
print('Image 2 captured.')
picam.switch_mode(pconfig)
time.sleep(5)
print("Stopping camera..")
picam.stop_preview()
picam.stop()

img1.show("Captured Image 1")
img2.show("Captured Image 2")

# same as above, using convenience methods
print("Starting camera..")
picam.start("preview", show_preview=True)
print('Say "cheese!"')
img1 = picam.switch_mode_and_capture_image("still", delay=1)
print('Image 1 captured.')
time.sleep(5)
print('Say "cheese!"')
img2 = picam.switch_mode_and_capture_image("still", delay=1)
print('Image 2 captured.')
time.sleep(5)
print("Stopping camera..")
picam.stop()

img1.show("Captured Image 1")
img2.show("Captured Image 2")
