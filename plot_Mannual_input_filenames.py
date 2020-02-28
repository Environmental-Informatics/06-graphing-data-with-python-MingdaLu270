#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 16:42:05 2020

@author: lu270
"""
## Mingda Lu

## Assignment 06 -- Graphing Data With Python -- last part

## plotting manual input files

## Feb 28, 2020


# import useful packages

import numpy as np
import matplotlib.pyplot as plt


# define the input file
print('Enter the file name which contains the data you want to plot')
fin=str(input())


# store data in a dataframe
df=np.genfromtxt(fin+'.txt', names=True)


x=df['Year']

# subplot 1, mean in black, max in red, and min in blue.

plt.subplot(311)
plt.plot(x,df['Mean'],'k',x,df['Max'],'r',x,df['Min'],'b')
plt.legend(["mean","Max","Min"],loc=0,prop={'size':4})
plt.xlabel('Year')
plt.ylabel('Streamflow (cfs)')


# subeplot 2, Tqmean*100

plt.subplot(312)
plt.plot(x,df['Tqmean']*100,'g^')
plt.xlabel('Year')
plt.ylabel('Tqmean (%)')

# subplot 3, bar chart

plt.subplot(313)
plt.bar(x,df['RBindex'])
plt.xlabel('Year')
plt.ylabel('R-B Index (ratio)')

# adjust the size

plt.subplots_adjust(hspace=0.6)



plt.savefig(fin+'.pdf')

plt.close()

print ('plotting completed')