import time

from picamera2 import Picamera2
from picamera2.encoders import H264Encoder


picam = Picamera2()

vconfig = picam.create_video_configuration()
picam.configure(vconfig)
encoder = H264Encoder(bitrate=5_000_000)
print("Smile, you're on camera.")
picam.start_preview()
picam.start_recording(encoder, "vid.h264")
time.sleep(10)
picam.stop_preview()
picam.stop_recording()
print('Video captured.')

# using convenience method
print("Smile, you're on camera.")
picam.start_and_record_video("vid.mp4", duration=10, show_preview=True)
print('Video captured.')
