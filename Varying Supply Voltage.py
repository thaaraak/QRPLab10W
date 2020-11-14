#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  3 08:32:51 2020

@author: pi
"""

import numpy as np
import matplotlib.pyplot as plt
import math


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

time12V, voltage12V = readcsv( "12.9-4V.csv" )
time14V, voltage14V = readcsv( "14.0-4V.csv" )
time16V, voltage16V = readcsv( "16.0-4V.csv" )
time18V, voltage18V = readcsv( "18.0-4V.csv" )
time20V, voltage20V = readcsv( "20.0-4V.csv" )

"""
rms = np.sqrt(np.mean(np.square(voltage3V)))
peak = np.max(voltage3V)
minpeak = np.min(voltage3V)

pwr_truerms = rms*rms/50
pwr_peakpeak = ((peak-minpeak)/2)**2/100
"""

plt.xlabel("Time" )
plt.ylabel("Voltage" )
plt.plot(time12V, voltage12V, label="12.9V")
plt.plot(time14V, voltage14V, label="14V")
plt.plot(time16V, voltage16V, label="16V")
plt.plot(time18V, voltage18V, label="18V")
plt.plot(time20V, voltage20V, label="20V")

plt.legend()
plt.show()
