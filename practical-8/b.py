import time

from picamera2 import Picamera2
from picamera2.encoders import H264Encoder
from picamera2.outputs import FfmpegOutput


picam = Picamera2()
encoder = H264Encoder(bitrate=5_000_000)
output = FfmpegOutput("vid.mp4")

vconfig = picam.create_video_configuration()
picam.configure(vconfig)
print("Smile, you're on camera.")
picam.start_preview(True)
picam.start_recording(encoder, output)
time.sleep(10)
picam.stop_preview()
picam.stop_recording()
print("Video captured.")

# using convenience method
# print("Smile, you're on camera.")
# picam.start_and_record_video("vid.mp4", duration=10, show_preview=True)
# print("Video captured.")
