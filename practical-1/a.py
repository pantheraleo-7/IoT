from gpiozero import LED


led = LED(13)

led.blink(background=False)
