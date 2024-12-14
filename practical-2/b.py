# pip install raspberrypi-tm1637
from tm1637 import TM1637


BRIGHTNESS = 3 # 0-7
DELAY = 100

display = TM1637(23, 24, BRIGHTNESS)

while True:
    display.scroll("Hello, World!", DELAY)
