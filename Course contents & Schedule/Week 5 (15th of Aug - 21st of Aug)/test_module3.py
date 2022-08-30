#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 14:56:16 2022

@author: brianparker
"""

# an example module of functions


def f(a):
    c = 3
    x = g(a) // 2
    return x

def g(a):
    d = 7
#    breakpoint()   
    return a * 4


# test module functions
if (__name__ == "__main__"):
    # __name__ is a global variable set to "__main__" only
    # when run as a script (and not when imported)
    print("f at 0=", f(0), "(Should be 0)")
    assert(f(0) == 0)
 

