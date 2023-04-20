# -*- coding: utf-8 -*-
"""
"""

import numpy as np
import matplotlib.pyplot as plt
import glob


datapath = 'C:/your/data/path/here//'
outpath = datapath

# x and y axis limits for data
qmin = 0.1
qmax = 0.8

#Y axis limits, can be turned on and off
Ymaxon = False
Ymin = 1000  # Only works when Ymaxon = True
Ymax = 10000 # Only works when Ymaxon = True

#normalisation factor, how far apart you want your individual profiles
#Set to 0 if you want no norm
Norm = 1000

###############################################################################
# Plot parameters
###############################################################################

# Plot title on/off?
plot_title = False

# File name as title of the plot?
File_name_as_title = True

# Custom plot title
custom_title = "insert custom plot title here"

# Title font size
title_font_size = 20

# Log axis?
Logx = False
Logy = False

# Axis titles
Xaxis = "q"
Yaxis = "I"
font_size = 8


#Legend options
Legend = True
Legend_Font  =8
Legend_Location = 'upper right'


###############################################################################
#Main script, dont touch
######################MAIN#####################################################

files = sorted(glob.glob(datapath+"*.dat"))
print("Dataset : ",)
print("Total number of files in data set : ",len(files))



fig, ax=plt.subplots()
counter =0
for data in files[0:5]:
    split_path = data.split("\\") 
    file_name = split_path[-1]
    file_tag = file_name[:-4] 
    print(file_tag)
    print("\n##################################################################################")
    print("plotting file: "+split_path[-1])
    print("##################################################################################")
    #print("counter1 is", counter)
    profile = np.loadtxt(data,skiprows=2)
    ax.set_facecolor("white")
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.plot(profile[:, 0], profile[:, 1]+counter, label =file_tag)
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
    counter = counter+Norm
    #print ("counter2 is", counter)
    if Legend == True:
        plt.legend(loc = Legend_Location, prop={'size': Legend_Font})
plt.savefig(outpath, dpi=300)
plt.show()

