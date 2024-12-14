import time
# pip install raspberrypi-tm1637
from tm1637 import TM1637


BRIGHTNESS = 3 # 0-7

display = TM1637(23, 24, BRIGHTNESS)

colon = True
while True:
    time.sleep(1 - time.time()%1)
    lt = time.localtime()
    display.numbers(lt.tm_hour, lt.tm_min, colon)
    colon = not colon
