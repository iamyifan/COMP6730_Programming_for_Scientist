#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 07:16:18 2022

@author: brianparker
"""
#-------
# numpy
#-------
# Examples based on https://numpy.org/doc/stable/user/absolute_beginners.html

import numpy as np

# one-dimensional vector
a = np.array([1, 2, 3, 4, 5, 6])

# two-dimensional array/vector
a2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

# indexing and slicing like built-in lists
a[1]
a[0:2]
a2[0,0]
a2[0:2,1:3]

# special matrices
np.zeros(2)
np.ones(2)
np.arange(4)

# underlying datatype can be specified (e.g. for processing image data)
# default is 64-bit floating point
x = np.ones(2, dtype=np.int64)

# can concatenate (join) arrays
x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6]]) 

np.concatenate((x, y), axis=0)
# also see vstack and hstack

# array dimensions
array_example = np.array([[[0, 1, 2, 3],
                           [4, 5, 6, 7]],

                           [[0, 1, 2, 3],  
                            [4, 5, 6, 7]],

                           [[0 ,1 ,2, 3], 
                            [4, 5, 6, 7]]])

array_example.ndim
array_example.size
array_example.shape

# reshaping array
a = np.arange(6)
np.reshape(a, newshape=(1, 6))

# vectorised expressions

# most operators are elementwise
data = np.array([1, 2])
ones = np.ones(2, dtype=int)
data + ones
data + ones + 7  # "broadcasting"

# matrix multiplication (not element-wise)
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
product = A @ B
# [[19 22]
#  [43 50]]

# reductions
a2.sum(axis=0)
# see also min max etc

# plotting
import matplotlib.pyplot as plt
x = np.linspace(0, 5, 20)
y = np.linspace(0, 10, 20)
plt.plot(x, y, 'red')




#--------
# pandas
#--------

import pandas as pd
from pandas import Series, DataFrame

s = Series([4,7,-5,3]) 

print(s)

print(s.values) 
print(type(s.values)) 

s = Series(range(5), index=list('abcde')) 

print(s) 

print(s.mean()) 

print(s+s)

df = DataFrame([[20.0,20.0],[21.0,30.0],[19.0,40.0]],columns = ['gene_experimental','gene_control']) 

print(df)
df.dtypes  # In a DataFrame columns can have different types

df[0:1]  # select rows
df.iloc[0:2, 0:1]  # slicing like list
df[df["gene_experimental"] > 20.0]  # index with a boolean expression (also for numpy)

# calculate average expression for each gene
print(df.mean())

# mean of gene_experimental column
print(df['gene_experimental'].mean()) 

# variance
print(df.var())

# read csv file
x = pd.read_csv('03-25-2022.csv', header=0)
x.head()


#----------------------
# handling missing data
#----------------------

s2 = s[1:]+s[:-1] 
print(s2)

# for missing completely at random (MCAR) data, we can unbiasedly exclude it 
print(s2.dropna()) 

# or we can impute missing data from surrounding data
print(s2.fillna(s2.mean()))

#---------
# scipy
#---------

from scipy import stats

# calculate p-value of differnce in gene expression across experimental conditions
# (using two independent sample t-test)
print(stats.ttest_ind(df.gene_experimental, df.gene_control))
# (p-value > 0.05 is NS- not statistically significant)









