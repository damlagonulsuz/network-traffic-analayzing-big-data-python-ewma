import math

import pyshark
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("C:/Users/damla/Desktop/Tez/Csvdosyaları/60sec.csv")

time_period = 60 # moving averages window

alpha = 2 / (time_period + 1) # smoothing factor

data['byte'].plot()

byteList = data['byte']


exponential_moving_average = [] # list used to store the computed exponential moving averages
exponential_moving_average_value = 0 # used to store the valur of the computed exponential moving average

for byte in byteList:
    if(exponential_moving_average_value == 0):
        exponential_moving_average_value = byte
    else:
        exponential_moving_average_value = alpha * byte + (1 - alpha) * exponential_moving_average_value

    exponential_moving_average.append(exponential_moving_average_value)

print(exponential_moving_average)

data = data.assign(Exponential_moving_average=pd.Series(exponential_moving_average, index=data.index))

fig1 = plt.figure(figsize=(10,8))
ax1 = fig1.add_subplot(111,ylabel='byte')
data['byte'].plot(ax=ax1, color='b', lw=3, legend=True)
data['Exponential_moving_average'].plot(ax=ax1, color='r', lw=3, legend=True)
plt.savefig('exponential_moving_average.png')
plt.show()

exponential_moving_average_pandas = data['byte'].ewm(span=time_period, adjust=False).mean()

fig2 = plt.figure(figsize=(10,8))
ax2 = fig2.add_subplot(111, ylabel='Byte')
data['Exponential_moving_average'].plot(ax=ax2, color='r', lw=10, label='Manually computed', legend=True)
exponential_moving_average_pandas.plot(ax=ax2, color='k', lw=3, label='Pandas ewm() function', legend=True)
plt.savefig('exponential_moving_average_comparison.png')
plt.show()