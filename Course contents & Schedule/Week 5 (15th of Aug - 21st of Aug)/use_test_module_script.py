#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 15:06:26 2022

@author: brianparker
"""

import test_module3

def my_func():
    my_data = 6   
    r = test_module3.f(my_data)      
    print("Twice ", my_data, " is ", r)

my_func()

#import test_module as tm

#print("Twice 2 is ", tm.f(2))


#from test_module import f

#print("Twice 2 is ", f(2))


