# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 15:16:06 2019

@author: Ben Guilfoyle - https://github.com/BenGfoyle

Overview:
"""
import matplotlib.pyplot as plt
    
def plotGraph(xAxis,yAxis,n1,n2):
    #Graphing and plotting, see matplot.lib library for more info (https://matplotlib.org/tutorials/introductory/sample_plots.html)
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.set_xlabel(n1)
    ax1.set_ylabel(n2)
    ax1.grid()
    ax1.plot(xAxis,yAxis)

sidHour = [17.25,17.5,17.75,18,18.25,18.5,18.75,19,19.25,19.5,19.75,20,20.25,20.5,20.75,21,21.25,21.5,21.75,22]  
elevation = [54.8061,57.03975,59.2607,61.4601,63.6261,65.7455,67.7925,69.7466,71.5700,73.2154,74.6208,75.7117,76.4092,76.65,76.4092,75.7115,74.6206,73.2151,71.5698,69.7463]
azimuth = [92.1414,95.3670,98.8210,102.5598,106.6553,111.1994,116.3091,122.1313,128.8431,136.6408,145.7014,156.1009,167.6901,180.0198,192.3115,203.9006,214.3,223.3605,231.1579,237.8696] 
print(len(sidHour))
print(len(elevation)) 
print(len(azimuth))
plotGraph(sidHour,elevation,"Sidereal","Elevation")
plotGraph(sidHour,azimuth,"Sidereal","Azimuth")
