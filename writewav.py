import wave
import numpy as np 
import matplotlib.pyplot as plt 
import struct

mulC0 = 17
fC0_1 = 470
ampC0_1 = [345,394,2100,90,50,62,0,40,0,63,0,0,46,58,50,20,35]
fC0_2 = 395
ampC0_2 = [265,71,588,167,65,83,60,0,0,23,37,0,110,0,0,0,0]
fC0_3 = 330
ampC0_3 = [110,0,304,219,167,65,155,0,60,50,0,0,0,35,0,0,0]

def genSignal(sp, f, a, ph, num):
    x = np.arange(0, num*1.0/sp, 1.0/sp)
    y = 2 * a * np.cos(2*np.pi*f*x + ph*np.pi/180)
    return y

def headConfig(nchannels=2, sampwidth=2, framerate=44100, nframes=0, comptype='NONE', name=''):
    return (nchannels, sampwidth, framerate, nframes, comptype, name)

def write():
    time = 1
    sp = 44100
    f = 470
    a = 300
    ph = 0
    num = time * sp
    mul = 17
    # x, y = genSignal(sp, f, a, ph, num)
    # plt.plot(x, y)
    # plt.show()
    y = np.zeros(num)
    for i in range(mul):
        y1 = genSignal(sp, fC0_1*(i+1), ampC0_1[i], ph, num)
        y2 = genSignal(sp, fC0_2*(i+1), ampC0_2[i], ph, num)
        y3 = genSignal(sp, fC0_3*(i+1), ampC0_3[i], ph, num)        
        y += y1 + y2 + y3
    y += genSignal(sp, 1403, 1352, ph, num)

    print y
    samples = []
    for i in range(num):
        samples.append(struct.pack('h', y[i]))
    sampleStr = ''.join(samples)
    filename = 'wave_' + str(f) + 'base_' + str(mul) + 'multiple.wav'
    wavefile = wave.open(filename, 'w')
    wavefile.setparams(headConfig(nframes = num*2, nchannels = 1))
    wavefile.writeframes(sampleStr)
    wavefile.close()
    print 'Write success'


if __name__ == '__main__':
    write()