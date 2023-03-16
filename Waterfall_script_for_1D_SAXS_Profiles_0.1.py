# -*- coding: utf-8 -*-
"""
author: Stefan Paporakis
"""
#############################################################################
#Script for plotting waterfall plots of SAXS data with a normalisation factor
#############################################################################



import glob
import numpy as np
import matplotlib.pyplot as plt



###############################################################################
#Input parameters
###############################################################################

#Where your data is stored
datapath = "Enter path to data here"
outpath = datapath


# x and y axis limits for data
qmin = 0.1
qmax = 0.8

#Y axis limits, can be turned on and off
Ymaxon = False
Ymin = 1000  # Only works when Ymaxon = True
Ymax = 10000 # Only works when Ymaxon = True

#normalisation factor, how far apart you want your individual profiles
Norm = 1000

###############################################################################
# Plot parameters
###############################################################################

# Plot title on/off?
plot_title = True

# File name as title of the plot?
File_name_as_title = True

# Custom plot title
custom_title = "insert custom plot title here"

# Title font size
title_font_size = 20

# Log axis?
Logx = False
Logy = True
# Axis titles

Xaxis = "q"
Yaxis = "I"
font_size = 16
#Legend options

Legend_Font  =20
Legend_Location = 'upper right'


###############################################################################
#Main script, dont touch
######################MAIN#####################################################
files = sorted(glob.glob(datapath+"*.dat"))
for data in files:
    split_path = data.split("\\") 
    file_name = split_path[-1]
    #File_title.append(file_name)
    file_tag = file_name[:-4]
    print (file_tag)
    profile = np.loadtxt(data,skiprows=2, delimiter = ",", max_rows = 605)
    fig, ax=plt.subplots()
    ax.set_facecolor("white")
    ax.plot(profile[:, 0], profile[:, 1], label = "23")
    ax.plot(profile[:, 0], profile[:, 2]+Norm, label = "30")
    ax.plot(profile[:, 0], profile[:, 3]+(2*Norm), label = "40")
    ax.plot(profile[:, 0], profile[:, 4]+(3*Norm), label = "50")
    ax.plot(profile[:, 0], profile[:, 5]+(4*Norm), label = "60")
    plt.legend(loc = Legend_Location, prop={'size': Legend_Font})
    if Logx == True:
        plt.xscale("log")
    if Logy ==True:
        plt.yscale("log")
    plt.xlim(qmin,qmax)
    if Ymaxon == True:
        plt.ylim(Ymin,Ymax)
    plt.xlabel(Xaxis, fontsize = font_size)
    plt.ylabel(Yaxis, fontsize = font_size)
    plt.grid(False)
    if plot_title is True and File_name_as_title is True:
        plt.title(split_path[-1],fontsize = title_font_size)
    if plot_title is True and File_name_as_title is False:
        plt.title(custom_title,fontsize = title_font_size)
    plt.savefig(datapath+file_tag)#, dpi=300)
    plt.show()
