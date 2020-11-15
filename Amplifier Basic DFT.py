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
        
    for k in range(0,dft_len):
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
time, voltage = readcsv( "data/SDS00024.csv" )
sig = voltage
  
#mag, re, im = calc_dft( sigs.ecg_signal )
mag, re, im = calc_dft( sig )
#mag = np.log10(mag)
inbuilt_fft = fft(sig)

f,plt_arr = plt.subplots(3, sharex=True)
f.suptitle( 'DFT' )

plt_arr[0].plot( sig[0:3500], color='red')
plt_arr[0].set_title('Signal')
plt_arr[1].plot( np.log10( np.abs(inbuilt_fft[0:3500])), color='green')
plt_arr[1].set_title('Inbuilt')
#plt_arr[2].plot( im, color='blue')
#plt_arr[2].set_title('Imaginary')
plt_arr[2].semilogy( mag, color='purple')
plt_arr[2].set_title('FFT Function')
