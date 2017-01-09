import wave
import numpy as np 
import matplotlib.pyplot as plt 
import struct

def genSignal(sp, f, a, ph, num):
    x = np.arange(0, num*1.0/sp, 1.0/sp)
    y = a * np.cos(2*np.pi*f*x + ph*np.pi/180)
    return x, y

def headConfig(nchannels=2, sampwidth=2, framerate=44100, nframes=0, comptype='NONE', name=''):
    return (nchannels, sampwidth, framerate, nframes, comptype, name)

def write():
    time = 2
    sp = 44100
    f = 440
    a = 3000
    ph = 0
    num = time * sp
    x, y = genSignal(sp, f, a, ph, num)
    # plt.plot(x, y)
    # plt.show()
    samples = []
    for i in range(num):
        samples.append(struct.pack('h', y[i]))
    sampleStr = ''.join(samples)
    wavefile = wave.open('test.wav', 'w')
    wavefile.setparams(headConfig(nframes = num*2, nchannels = 1))
    wavefile.writeframes(sampleStr)
    wavefile.close()
    print 'Write success'


if __name__ == '__main__':
    write()