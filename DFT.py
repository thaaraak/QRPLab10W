from matplotlib import pyplot as plt
from scipy import signal
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




#sig1 = [ 0.3*math.sin( 2*math.pi*i/13) + math.sin(2*math.pi*i/94) for i in range(0,1000)]
#plt.plot(sig1)

sampling_rate = 2000
nyq_freq = sampling_rate / 2

t = np.linspace(0, 1, sampling_rate)

sig_5hz = np.sin( 2*np.pi*5*t )
sig_7hz = np.sin( 2*np.pi*7*t )
sig_30hz = np.sin( 2*np.pi*30*t )
sig_50hz = np.sin( 2*np.pi*50*t )
sig_250hz = np.sin( 2*np.pi*250*t )

sig = sig_250hz #* sig_250hz
  
#mag, re, im = calc_dft( sigs.ecg_signal )
mag, re, im = calc_dft( sig )

f,plt_arr = plt.subplots(4, sharex=True)
f.suptitle( 'DFT' )

plt_arr[0].plot( sig, color='red')
plt_arr[0].set_title('Signal')
plt_arr[1].plot( re, color='green')
plt_arr[1].set_title('Real')
plt_arr[2].plot( im, color='blue')
plt_arr[2].set_title('Imaginary')
plt_arr[3].plot( mag, color='purple')
plt_arr[3].set_title('Magnitude')
