import time

from gpiozero import LED


gpio_pins = (5, 13, 21)
leds = [LED(pin) for pin in gpio_pins]

while True:
    for led in leds:
        led.on()
        time.sleep(0.2)
        led.off()
    for led in reversed(leds):
        led.on()
        time.sleep(0.2)
        led.off()
