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
            ang[i] = math.atan(arr.imag / arr.real)
    return freq, amp, ang 


plt.figure(1)
ax1 = plt.subplot(511)
ax2 = plt.subplot(512)
ax3 = plt.subplot(513)
ax4 = plt.subplot(514)
ax5 = plt.subplot(515)

plt.sca(ax1)
x1, y1 = sample(1000)
plt.plot(x1, y1)
plt.title("original")

plt.sca(ax2)
y1fft = np.fft.fft(y1) / len(y1)
x2, y2 = freqSpec(1000, y1fft)
plt.plot(x2, y2, 'o')
plt.title("frequence")

plt.sca(ax3)
x3, y3 = sample(120)
plt.plot(x3, y3)
plt.title("sf = 120Hz")

plt.sca(ax4)
y3fft = np.fft.fft(y3) / len(y3)
x4, y4 = freqSpec(120, y3fft)
plt.plot(x4, y4, 'o')

plt.sca(ax5)
y5 = np.fft.ifft(y3fft)
plt.plot(x3, y5)

plt.show()