import time

from gpiozero import LED


leds = [LED(pin) for pin in (5, 13, 21)]

while True:
    for led in leds:
        led.on()
        time.sleep(0.2)
        led.off()
    for led in reversed(leds):
        led.on()
        time.sleep(0.2)
        led.off()
