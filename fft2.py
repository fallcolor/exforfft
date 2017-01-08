import numpy as np 

def func(sp):
    x = np.arange(0, 1, 1/sp)
    y = 2 + 3*np.cos(2*np.pi*50*x - np.pi/6) + 1.5*np.cos(2*np.pi*75*x + np.pi/2)
    return x, y

def fftvalue(arr):
    return np.fft.fft(arr)

sp = 256