import numpy as np 
import matplotlib.pyplot as plt 

x = np.arange(-10, 10, 0.01)

y = np.empty(len(x))

for i in range(len(x)):
    if np.sin(x[i]) < 0:
        y[i] = 0;
    else:
        y[i] = 1

plt.figure(1)
ax1 = plt.subplot(311)
ax2 = plt.subplot(312)
ax3 = plt.subplot(313)

plt.sca(ax1)
plt.plot(x, y)

plt.sca(ax2)
y0 = np.fft.fft(y)
plt.plot(y0)

plt.sca(ax3)
plt.plot(x, np.fft.ifft(y0))

plt.show()