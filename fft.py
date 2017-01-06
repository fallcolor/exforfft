import numpy as np 
import matplotlib.pyplot as plt 
import math

def sample(f):
    ''' return x and y between [-0.1s, 0.1s] according to sample frequency
    '''
    x = np.linspace(-0.1, 0.1, f/5)
    y = np.sin(2*np.pi*60*x) + np.cos(2*np.pi*25*x) + np.cos(2*np.pi*30*x)
    return x, y

def freqSpec(sf, arr):
    ''' return frequency spectrum
    '''
    l = (int)(math.floor(len(arr)/2) + 1)

    x = np.empty(l)
    y = np.empty(l)

    for i in range(l):
        x[i] = i * sf / len(arr)

    y = np.abs(arr)[:l]
    for i in range(len(y)):
        if y[i] < 0.05:
            y[i] = 0

    return x, y

def freq2time(sf, arr):
    freq, amp = freqSpec(sf, arr)
    ang = np.empty(len(freq))
    for i in range(len(freq)):
        if amp[i] > 0:
            ang[i] = math.atan(arr[i].imag / arr[i].real)
    return freq, amp, ang 

def funci(freq, amp, ang, pointnum):
    x = np.linspace(-0.1, 0.1, pointnum)
    y = np.empty(pointnum)
    for i in range(pointnum):
        y[i] = 0
        for j in range(len(freq)):
            if amp[j] > 0:
                y[i] += 2 * amp[j] * np.cos(2 * np.pi * freq[j] * x[i] + ang[j])
    return x, y

def plotdata(sp, disnum):
    x, y = sample(sp)
    yfft = np.fft.fft(y) / len(y)
    freq, amp, ang = freq2time(sp, yfft)
    xo, yo = funci(freq, amp, ang, disnum)
    return freq, amp, xo, yo

plt.figure(1)
ax0 = plt.subplot(421)
ax1 = plt.subplot(422)
ax2 = plt.subplot(423)
ax3 = plt.subplot(424)
ax4 = plt.subplot(425)
ax5 = plt.subplot(426)
ax6 = plt.subplot(427)
ax7 = plt.subplot(428)

plt.sca(ax1)
x1, y1 = sample(1000)
plt.plot(x1, y1)
plt.title("original")

freq2, amp2, x2, y2 = plotdata(80, 1000)
plt.sca(ax2)
plt.stem(freq2, amp2)
plt.title("80Hz freq")

plt.sca(ax3)
plt.plot(x2, y2)

freq3, amp3, x3, y3 = plotdata(100, 1000)
plt.sca(ax4)
plt.stem(freq3, amp3)
plt.title("100Hz freq")

plt.sca(ax5)
plt.plot(x3, y3)

freq4, amp4, x4, y4 = plotdata(1200, 1000)
plt.sca(ax6)
plt.stem(freq4, amp4)
plt.title("120Hz freq")

plt.sca(ax7)
plt.plot(x4, y4)

plt.show()