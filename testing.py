import matplotlib.pyplot as plt
import numpy as np
import math 

timesteps = 1000
resolution = 100 # timestep resolution as seconds/resolution e.g. resolution of 10 means 1/10 so 100ms
freqStep = 100 # number of frequencies computed
freqRes = 10 # timestep resolution as freq/resolution e.g. resolution of 10 means 1/10 so 0.1 hz steps
pi = 3.14159265359


a = [0] * timesteps     # amplitude of signal
time = [0] * timesteps  # time of signal
Xf = [0] * freqStep     # fourier transform output
fplot = [0] * freqStep  # frequency range to plot


for t in range(timesteps):
    #a[t] = math.sin(t/resolution)  #calulating amplitude of signal
    a[t] = (2 * math.sin(2*pi*2*(t/resolution))) + (1 * math.sin(2*pi*4*(t/resolution))) + (0.5 * math.sin(2*pi*9*(t/resolution))) #calulating amplitude of signal
    time[t] = t/resolution

for f in range (freqStep):
    FTint = 0
    freq = f/freqRes
    fplot[f] = freq
    real = 0
    imag = 0

    for t in range(timesteps):
        #i = math.sqrt((a[t] * math.cos(2*pi*freq))**2+(math.sin(2*pi*freq))**2)
        tim = t/resolution
        #FTint += a[t] * ((math.cos(2*pi*freq*tim))-  (math.sqrt((a[t] * math.cos(2*pi*freq*tim))**2+(math.sin(2*pi*freq*tim))**2)  * (math.sin(2*pi*freq*tim))))
        dt = 1/resolution
        angle = 2*pi*freq*tim
        real += a[t] * math.cos(angle) * dt
        imag -= a[t] * math.sin(angle) * dt
    
    Xf[f] = math.sqrt(real**2 + imag**2)



plt.plot(time, a)
plt.show()
plt.plot(fplot, Xf)
plt.show()