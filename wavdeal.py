import wave
import struct
import numpy as np 
import fft
import matplotlib.pyplot as plt 

filename = 'test.wav'
# filename = 'voilin.wav'

wavefile = wave.open(filename, 'r')

nchanells = wavefile.getnchannels()
sampltWidth = wavefile.getsampwidth()
framerate = wavefile.getframerate()
numframes = wavefile.getnframes()

print 'channels:     ', nchanells
print 'sample width: ', sampltWidth
print 'frame rate:   ', framerate
print 'num frames:   ', numframes

if numframes > 100:
    numframes = 100

x = np.linspace(0, numframes*1.0/framerate, numframes)
y = np.zeros(numframes)

# print len(x), len(y)

# get amplitude
for i in range(numframes):  
    val = wavefile.readframes(1)  
    left = val[0:2]
    right = val[2:4]
    v = struct.unpack('h', left )[0]  
    y[i] = v

# for i in range(len(x)):
#     print x[i], y[i]

ax1 = plt.subplot(211)
ax2 = plt.subplot(212)

plt.sca(ax1)
plt.plot(x, y)
plt.xlim(0, numframes*1.0/framerate)

yfft = np.fft.fft(y)/len(y)
freq, amp, ang = fft.freq2time(framerate, yfft)

plt.sca(ax2)
plt.stem(freq, amp)
plt.stem(freq, ang, markerfmt = 'x')

plt.show()