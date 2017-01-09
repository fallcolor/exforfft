import wave
import numpy as np 
import matplotlib.pyplot as plt 

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
    a = 80
    ph = 0
    num = time * sp
    x, y = genSignal(sp, f, a, ph, num)
    plt.plot(x, y)
    plt.show()
    # yfinal = np.zeros(num*2)
    yfinal = []
    for i in range(num):
        tmp = (int)(y[i])
        # yfinal[i*2] = tmp % 256
        # yfinal[i*2+1] = tmp / 256
        yfinal.append(tmp%256)
        yfinal.append(tmp/256)
        print yfinal[i*2], yfinal[i*2+1]
    wavefile = wave.open('test.wav', 'w')
    wavefile.setparams(headConfig(nframes = num*2, nchannels = 1))
    wavefile.writeframes(yfinal)
    wavefile.close()
    print 'Write success'


if __name__ == '__main__':
    write()