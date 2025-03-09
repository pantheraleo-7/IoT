from collections import deque
# pip install adafruit-circuitpython-ads1x15 matplotlib
import board
import numpy as np
import matplotlib.pyplot as plt
from adafruit_ads1x15 import ads1x15
from adafruit_ads1x15.ads1115 import ADS1115
from adafruit_ads1x15.analog_in import AnalogIn
from matplotlib.animation import FuncAnimation


DURATION = 10
SAMPLE_RATE = 16 # 8, 16, 32, 64, 128, 250, 475, 860
GAIN = 4 # 2/3, 1, 2, 4, 8, 16
CHANNELS = (0, None) # Single-ended read
#CHANNELS = (0, 1) # Differential read between channels 0 and 1

i2c = board.I2C()
ads = ADS1115(i2c, GAIN, SAMPLE_RATE, ads1x15.Mode.CONTINUOUS)
chan = AnalogIn(ads, *CHANNELS) # ADS1115 has 4 input channels: 0, 1, 2, 3

num_samples = SAMPLE_RATE*DURATION
x = np.linspace(0, DURATION, num_samples)
y = deque(0.0 for _ in range(num_samples))

fig, ax = plt.subplots()
ax.grid(True)
ax.set_xlim(0, DURATION+1)
ax.set_ylim(-7, 7)
ax.set_xlabel("Time [s]")
ax.set_ylabel("Voltage [V]")
ax.set_title("Real-Time Oscilloscope Simulation")
line, = ax.plot(x, y, marker="o", markevery=[-1])


def update(_frame):
    y.popleft()
    y.append(chan.voltage)
    line.set_ydata(y)

    return line,


anim = FuncAnimation(fig, update, frames=num_samples, interval=1000/SAMPLE_RATE, blit=True)
plt.show()
