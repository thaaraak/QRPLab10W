#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  3 08:32:51 2020

@author: pi
"""

import numpy as np
import matplotlib.pyplot as plt
import math

# Original Filter
# 0.02 V on Signal Generator

inputvoltage=[.8, 1, 1.2, 1.4, 2.0, 2.2, 2.4, 2.8, 3.0, 3.2, 3.6, 3.8, 4.0, 4.2, 4.8, 5.0, 5.2, 6.0, 7.0 ]
#outpower13v=[ .34, .51, .71, .94, 1.85, 2.2, 2.58, 3.37, 3.79, 4.17, 4.88, 5.24, 5.59, 5.76, 6.96, 7.39, 7.84, 9.98, 13.83 ]
#outpower20v=[ .34, .51, .7, .94, 1.88, 2.25, 2.69, 3.61, 4.19, 4.75, 6.03, 6.73, 7.45, 8.2, 10.24, 10.62, 11.28, 13.83, 16.64  ]

peakpeak13v= [ 11.2, 13.6, 16.0, 18.4, 26.4, 28.4, 31.2, 35.2, 37.6, 39.2, 42.4, 44.0, 45.6, 48.0, 52.8, 54.4, 56.0, 63.2, 74.4 ]
peakpeak20v= [ 11.2, 13.6, 16.0, 18.4, 26.4, 28.8, 31.2, 36.8, 39.2, 42.0, 47.6, 50.4, 52.8, 56.4, 64.0, 65.6, 67.2, 74.4, 81.6 ]

pkpk13vlpf = [ 10.4, 12.8, 15.2, 17.6, 24.8, 27.2, 29.6, 34.4, 36.4, 38.4, 42.4, 44.4, 46.4, 48.0, 53.6, 55.2, 56.8, 63.6, 69.6 ]
pkpk20vlpf = [ 10.4, 12.8, 15.2, 17.6, 25.2, 28.0, 30.4, 35.2, 38.4, 40.8, 46.4, 48.0, 52.8, 54.0, 61.6, 64.0, 67.2, 74.8, 83.2 ]

f, parr = plt.subplots( 1, sharex=True)

outputpower13v = [ e*e / 100 for e in peakpeak13v ]
outputpower20v = [ e*e / 100 for e in peakpeak20v ]
outputpower13vlpf = [ e*e / 100 for e in pkpk13vlpf ]
outputpower20vlpf = [ e*e / 100 for e in pkpk20vlpf ]

plt.xlabel("Peak to Peak Input Voltage" )
plt.ylabel("Peak to Peak Output" )
plt.plot(inputvoltage, pkpk13vlpf, label="13V LPF")
plt.plot(inputvoltage, peakpeak13v, label="13V")
plt.plot(inputvoltage, pkpk20vlpf, label="20V LPF")
plt.plot(inputvoltage, peakpeak20v, label="20V")
plt.legend()

"""
parr[0].plot(inputvoltage, peakpeak13v)
parr[0].set_title( "Peak-peak at 13.8V" )
parr[0].set_xlabel("Input Voltage" )
parr[0].set_ylabel("Sqrt(Output Power)" )

parr[1].plot(inputvoltage, peakpeak20v)
parr[1].set_title( "Peak-peak at 20.0V" )
parr[1].set_xlabel("Input Voltage)" )
parr[1].set_ylabel("Sqrt(Output Power)" )

parr[0].grid()
parr[1].grid()
"""
plt.show()

"""
parr[0].plot(np.log10( inputvoltage), np.log10(outpower13v))
parr[0].set_title( "Output Power at 13.8V" )
parr[0].set_xlabel("Log(Input Voltage)" )
parr[0].set_ylabel("Log(Output Power)" )

parr[1].plot(np.log10( inputvoltage), np.log10(outpower20v))
parr[1].set_title( "Output Power at 20.0V" )
parr[1].set_xlabel("Log(Input Voltage)" )
parr[1].set_ylabel("Log(Output Power)" )

parr[0].grid()
parr[1].grid()
plt.show()
"""