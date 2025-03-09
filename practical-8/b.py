import time

from picamera2 import Picamera2
from picamera2.encoders import H264Encoder
from picamera2.outputs import FfmpegOutput


picam = Picamera2()
output = FfmpegOutput("video.mp4")
encoder = H264Encoder(bitrate=5_000_000)

vconfig = picam.create_video_configuration()
picam.configure(vconfig)

picam.start_preview(True)
picam.start()

print("Taking video...")
picam.start_recording(encoder, output)
time.sleep(10)
picam.stop_recording()
print("Video captured")

picam.stop_preview()
picam.stop()

# using convenience method
# print("Taking video...")
# picam.start_and_record_video("video.mp4", duration=10, show_preview=True)
# print("Video captured")

picam.close()
