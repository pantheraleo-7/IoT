import signal

from gpiozero import Button, LED


button = Button(5)
led = LED(13)

led.source = button

signal.pause()
