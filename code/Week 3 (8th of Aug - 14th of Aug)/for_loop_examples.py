#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 23:27:32 2022

@author: brianparker
"""

# for loops are ideal for interating a fixed number of times
print("for loop example")
for i in range(0,10):
    print(i)
   
# we can always emulate a for loop with a while loop and a count variable,
# but it is wordier and less clear    
print("while loop example")    
j = 0
while j < 10:
    print(j)
    j = j + 1

# for loops in python are also ideal for iterating over all (or part) of a 
# sequence data type like list (this is a prelude to the next lectures 
# on built-in data types)
print("list example")    
a = ["one", "two", "three"]
for c in a:
    print(c)

# sometimes we want the position (or index) of an element as well as its value.
# python has a syntax for that
for indx,c in enumerate(a):
    print(indx)
    print(a[indx])
    
