import numpy as np 
import matplotlib.pyplot as plt 
import math

def sample(f):
    ''' return x and y between [-0.1s, 0.1s] according to sample frequency
    '''
    if f == 0:
        return 0, 0
    x = np.arange(-0.1, 0.1, 1.0/f)
    # y = np.sin(2*np.pi*60*x) + np.cos(2*np.pi*25*x) + np.cos(2*np.pi*30*x)
    y = 2 + 3*np.cos(2*np.pi*50*x-np.pi/6) + 1.5*np.cos(2*np.pi*75*x+np.pi/2)
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
    # print y 
    # print 'len freq:  ', len(y)
    # for i in range(len(y)):
    #     if y[i] < 0.05:
    #         y[i] = 0

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
            # if amp[j] > 0:
            y[i] += 2 * amp[j] * np.cos(2 * np.pi * freq[j] * x[i] + ang[j])
        # y[0] = 2 * amp[0]
    return x, y

def plotdata(sp, disnum):
    x, y = sample(sp)
    yfft = np.fft.fft(y) / len(y)
    # print 'sample number: ', len(y)
    # print 'fft number:    ', len(yfft)
    freq, amp, ang = freq2time(sp, yfft)
    xo, yo = funci(freq, amp, ang, disnum)
    print 'sample freq: ', sp
    for i in range(len(freq)):
        print 'freq:  ', freq[i]
        print 'fft:   ', yfft[i]
        print 'amp:   ', amp[i]
        print 'ang:   ', ang[i]
    return freq, amp, ang, xo, yo

plt.figure(1)
ax0 = plt.subplot(321)
ax1 = plt.subplot(322)
ax2 = plt.subplot(323)
ax3 = plt.subplot(324)
ax4 = plt.subplot(325)
ax5 = plt.subplot(326)

plt.sca(ax0)
freq1 = [0, 50, 75]
amp1 = [2, 3, 1.5]
ang1 = [0, -np.pi/6, np.pi/2]
plt.stem(freq1, amp1)
plt.stem(freq1, ang1, markerfmt = 'x')
plt.title("original")

plt.sca(ax1)
x1, y1 = sample(1000)
plt.plot(x1, y1)

f2 = 80
freq2, amp2, ang2, x2, y2 = plotdata(f2, 1000)
plt.sca(ax2)
plt.stem(freq2, amp2)
plt.stem(freq2, ang2, markerfmt = 'x')
plt.title(str(f2) + "Hz freq")

plt.sca(ax3)
plt.plot(x2, y2)
plt.xlim(-0.1, 0.1)

f3 = 200
freq3, amp3, ang3, x3, y3 = plotdata(f3, 1000)
plt.sca(ax4)
plt.stem(freq3, amp3)
plt.stem(freq3, ang3, markerfmt = 'x')
plt.title(str(f3) + "Hz freq")
plt.legend()

plt.sca(ax5)
plt.plot(x3, y3)
plt.xlim(-0.1, 0.1)

plt.show()