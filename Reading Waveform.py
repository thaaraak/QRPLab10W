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

time3V, voltage3V = readcsv( "SDS00019.csv" )
time4V, voltage4V = readcsv( "SDS00020.csv" )
time5V, voltage5V = readcsv( "SDS00021.csv" )
time6V, voltage6V = readcsv( "SDS00022.csv" )

rms = np.sqrt(np.mean(np.square(voltage3V)))
peak = np.max(voltage3V)
minpeak = np.min(voltage3V)

pwr_truerms = rms*rms/50
pwr_peakpeak = ((peak-minpeak)/2)**2/100

plt.subplot(2, 1, 1)
plt.xlabel("Time" )
plt.ylabel("Voltage" )
plt.plot(time3V, voltage3V, label="3V")
plt.plot(time4V, voltage4V, label="4V")
plt.plot(time5V, voltage5V, label="5V")
plt.plot(time6V, voltage6V, label="6V")

#plt.legend()
#plt.show()

time3V, voltage3V = readcsv( "12.9V-3V-Input" )
time4V, voltage4V = readcsv( "12.9V-4V-Input" )
time5V, voltage5V = readcsv( "12.9V-5V-Input" )
time6V, voltage6V = readcsv( "12.9V-6V-Input" )

rms = np.sqrt(np.mean(np.square(voltage3V)))
peak = np.max(voltage3V)
minpeak = np.min(voltage3V)

pwr_truerms = rms*rms/50
pwr_peakpeak = ((peak-minpeak)/2)**2/100

plt.subplot(2, 1, 2)
plt.xlabel("Time" )
plt.ylabel("Voltage" )
plt.plot(time3V, voltage3V, label="3V")
plt.plot(time4V, voltage4V, label="4V")
plt.plot(time5V, voltage5V, label="5V")
plt.plot(time6V, voltage6V, label="6V")

plt.legend()
plt.show()