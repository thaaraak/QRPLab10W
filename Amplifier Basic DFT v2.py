from matplotlib import pyplot as plt
from scipy import signal
from scipy import fft
import math
import numpy as np

def calc_dft( sig ):
    
    sig_len = len(sig)
    dft_len = int(sig_len/2+1)

    re = [0.0] * dft_len
    im = [0.0] * dft_len
    mag = [0.0] * dft_len

    for k in range(0, dft_len):
        
        for i in range(0,sig_len):
            re[k] += sig[i]*math.cos( 2*math.pi*k*i / sig_len)
            im[k] -= sig[i]*math.sin( 2*math.pi*k*i / sig_len)

        mag[k] = math.sqrt( re[k]**2 + im[k]**2 )    

    return mag, re, im


import csv


def readcsv( inpfile ):
       
    time = []
    voltage = []

    with open(inpfile) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
    
        for row in csv_reader:
        
            if line_count < 3:
                line_count += 1
            
            else:
                time.append( float(row[0]) )
                voltage.append( float(row[1]) )
            
            line_count += 1

    return time, voltage            


time, voltage = readcsv( "data/SDS00019.csv" )
time, voltage = readcsv( "data/12.9-3V-lpf.csv" )
time, voltage = readcsv( "data/SDS00026.csv" )
  
#mag, re, im = calc_dft( sigs.ecg_signal )

numpts = int(len(voltage)/2)

sample_rate = time[1] - time[0]
nyquist_rate = 2 * sample_rate
hz_per_point = 1 / ( nyquist_rate * numpts )
max_freq = int(1 / nyquist_rate / 1000000)

mag, re, im = calc_dft( voltage )
freq = np.linspace(0, max_freq, numpts+1)

inbuilt_fft = fft(voltage)



plt.figure(1)
plt.xlabel("Frequency (MHz)" )
plt.ylabel("log10(Mag)" )
plt.semilogy( freq, mag )

plt.figure(3)
plt.xlabel("Frequency (MHz)" )
plt.ylabel("log10(Mag)" )
plt.semilogy( freq, np.abs(inbuilt_fft[0:numpts+1]) )

plt.figure(2)
plt.xlabel("Time" )
plt.ylabel("Voltage" )
plt.plot( time[0:1000], voltage[0:1000] )

plt.show()