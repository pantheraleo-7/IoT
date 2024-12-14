import time

from gpiozero import LED


led = LED(13)

while True:
    led.on()
    time.sleep(0.5)
    led.off()
    time.sleep(0.5)
