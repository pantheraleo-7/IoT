import time

from picamera2 import Picamera2


picam = Picamera2()

pconfig = picam.create_preview_configuration()
sconfig = picam.create_still_configuration()
picam.configure(pconfig)

picam.start_preview(True)
picam.start()

picam.switch_mode(sconfig)
print("Taking image...")
time.sleep(1)
img1 = picam.capture_image()
print("Image 1 captured")

picam.switch_mode(pconfig)
time.sleep(5)

picam.switch_mode(sconfig)
print("Taking image...")
time.sleep(1)
img2 = picam.capture_image()
print("Image 2 captured")

picam.switch_mode(pconfig)
time.sleep(5)

picam.stop_preview()
picam.stop()

# using convenience methods
# picam.start("preview", show_preview=True)
# print("Taking image...")
# img1 = picam.switch_mode_and_capture_image("still", delay=1)
# print("Image 1 captured")
# time.sleep(5)
# print("Taking image...")
# img2 = picam.switch_mode_and_capture_image("still", delay=1)
# print("Image 2 captured")
# time.sleep(5)
# picam.stop()

picam.close()

img1.show("Image 1")
img2.show("Image 2")
