import time
# pip install raspberrypi-tm1637
import tm1637


display = tm1637.TM1637(23, 24)

colon = True
while True:
    time.sleep(1 - time.time()%1)
    lt = time.localtime()
    display.numbers(lt.tm_hour, lt.tm_min, colon)
    colon = not colon
