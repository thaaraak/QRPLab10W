from matplotlib import pyplot as plt
from scipy import signal
from scipy import fft
import math
import numpy as np
from scipy.signal import hilbert, chirp
from scipy.signal import butter, lfilter, freqz
import statistics

def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def butter_lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y

def moving_average(x, w):
    return np.convolve(x, np.ones(w), 'valid') / w


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


def readcsv( inpfile, rows ):
       
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
            if rows > 0 and line_count > rows:
                break

    return time, voltage             


#time, voltage = readcsv( "/home/xenir/Downloads/SDS00004.csv", 2000 )
time, voltage = readcsv( "/home/xenir/Downloads/SDS00009.csv", 100000 )
#time, voltage = readcsv( "data/12.9-3V-lpf.csv" )
#time, voltage = readcsv( "data/SDS00028.csv" )
  
numpts = int(len(voltage)/2)
#numpts = int(len(voltage))

sample_rate = time[1] - time[0]
nyquist_rate = 2 * sample_rate
hz_per_point = 1 / ( nyquist_rate * numpts )
max_freq = int(1 / nyquist_rate / 1000000)

signal = voltage
analytic_signal = hilbert(signal)
amplitude_envelope = np.abs(analytic_signal)
amplitude_envelope = moving_average(amplitude_envelope, 100)

audio_sample_rate = 44100
audio_sample_adjust = int(( 1.0 / audio_sample_rate ) / sample_rate)

total_audio_samples = int( len(voltage) / audio_sample_adjust )
audio_samples = [0.0] * total_audio_samples

for i in range(0, total_audio_samples):
    audio_samples[i] = amplitude_envelope[ i*audio_sample_adjust ]

dc_component = statistics.mean( audio_samples )
audio_samples = audio_samples - dc_component

mag, re, im = calc_dft( audio_samples )
freq = np.linspace(0, 44100/2.0, int(total_audio_samples/2+1))
mag = np.divide(mag, len(freq))
mag = np.divide( np.power( mag, 2 ), 100 )
mag = np.multiply( np.log10( mag ), 10 )


"""
mag, re, im = calc_dft( voltage )
freq = np.linspace(0, max_freq, numpts+1)

#inbuilt_fft = fft(voltage)

mag = np.divide(mag, numpts)
mag = np.divide( np.power( mag, 2 ), 100 )
mag = np.multiply( np.log10( mag ), 10 )

# Add -50db for attenuator + 30 to convert to dBm = -20
#mag = np.add( mag, -20 )
"""

plt.figure(1)
plt.xlabel("Time" )
plt.ylabel("Amplitude" )
#plt.plot( freq, mag )
plt.plot( analytic_signal )
plt.plot( amplitude_envelope )

plt.figure(2)
plt.xlabel("Time" )
plt.ylabel("Amplitude" )
plt.plot( audio_samples )

plt.figure(3)
plt.xlabel("Frequency (MHz)" )
plt.ylabel("Power (dBm)" )
plt.plot( freq[1:], mag[1:] )

"""
plt.figure(3)
plt.xlabel("Frequency (MHz)" )
plt.ylabel("log10(Mag)" )
plt.semilogy( freq, np.abs(inbuilt_fft[0:numpts+1]) )

plt.figure(2)
plt.xlabel("Time" )
plt.ylabel("Voltage" )
plt.plot( time[0:1000], voltage[0:1000] )
"""

plt.show()
