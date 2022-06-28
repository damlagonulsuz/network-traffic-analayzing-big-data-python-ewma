import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("C:/Users/damla/Desktop/60sec.csv")


print(data.head())

time_period = 60
alpha = 0.8 # smoothing factor

data['Length'].plot()


byteList = data['Length']


exponential_moving_average = [] # list used to store the computed exponential moving averages
exponential_moving_average_value = 0 # used to store the value of the computed exponential moving average

for byte in byteList:
    if(exponential_moving_average_value == 0):
        exponential_moving_average_value = byte
    else:
        exponential_moving_average_value = alpha * byte + (1 - alpha) * exponential_moving_average_value

    exponential_moving_average.append(exponential_moving_average_value)



# Manually computed plot

data = data.assign(Exponential_moving_average=pd.Series(exponential_moving_average, index=data.index))

# fig1 = plt.figure(figsize=(10, 8))
# ax1 = fig1.add_subplot(111, ylabel='Length', xlabel='Traffic')
# data['Length'].plot(ax=ax1, color='b', lw=3, legend=True)
# data['Exponential_moving_average'].plot(ax=ax1, color='r', lw=3, legend=True)
# plt.savefig('exponential_moving_average_alpha_0.8.png')
# plt.show()


# EWMA computed with pandas function and manually computed values comparison

exponential_moving_average_pandas = data['Length'].ewm(span=time_period, adjust=False).mean()

# fig2 = plt.figure(figsize=(10, 8))
# ax2 = fig2.add_subplot(111, ylabel='Length')
# data['Exponential_moving_average'].plot(ax=ax2, color='r', lw=10, label='Manually computed', legend=True)
# exponential_moving_average_pandas.plot(ax=ax2, color='k', lw=3, label='Pandas ewm() function', legend=True)
# plt.savefig('exponential_moving_average_comparison_alpha_0.8.png')
# plt.show()




# fig3 = plt.figure(figsize=(10, 8))
# ax3 = fig3.add_subplot(111, ylabel='Length')
# data['Length'].plot(ax=ax3, color='r', lw=10, label='Actual Length', legend=True)
# exponential_moving_average_pandas.plot(ax=ax3, color='k', lw=3, label='Pandas ewm() function', legend=True)
# plt.savefig('exponential_moving_average_comparison_with_length_alpha_0.8_pandas.png')
# plt.show()



# fig4 = plt.figure(figsize=(10, 8))
# ax4 = fig4.add_subplot(111, ylabel='Length')
# data['Length'].plot(ax=ax4, color='r', lw=10, label='Actual Length', legend=True)
# exponential_moving_average_pandas.plot(ax=ax4, color='k', lw=3, label='Manually computed', legend=True)
# plt.savefig('exponential_moving_average_comparison_with_length_alpha_0.8_manually.png')
# plt.show()