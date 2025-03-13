import time
from collections import deque

from gpiozero import LEDBoard


leds = LEDBoard(5, 6, 13, 19, 26)
state = deque((1, 0, 0, 0, 0))
direction = 1

while True:
    for _ in range(len(leds)-1):
        leds.value = state
        time.sleep(0.2)
        state.rotate(direction)
    direction *= -1
