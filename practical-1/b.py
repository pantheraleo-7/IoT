import signal

from gpiozero import Button, LED


button = Button(5)
led = LED(13)

button.when_pressed = led.on
button.when_released = led.off

signal.pause()
