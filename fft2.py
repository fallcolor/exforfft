import numpy as np 
import math

def func(sp, dr):
    x = np.arange(0, dr, 1.0/sp)
    y = 2 + 3*np.cos(2*np.pi*50*x - np.pi/6) + 1.5*np.cos(2*np.pi*75*x + np.pi/2)
    return x, y

def fftvalue(arr):
    return np.fft.fft(arr)/len(arr)

sp = 2560
dr = 0.1

x, y = func(sp, dr)
ffty = fftvalue(y)

for i in range(len(y)/2 + 1):
    print 'req:   ', i
    print 'value: ', ffty[i]
    print 'amp:   ', np.abs(ffty[i])
    print 'ang:   ', math.atan(ffty[i].imag/ffty[i].real)/np.pi * 180
    print ' '