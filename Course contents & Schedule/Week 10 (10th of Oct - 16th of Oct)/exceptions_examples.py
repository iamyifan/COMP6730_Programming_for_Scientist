#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 12:22:41 2022

@author: brianparker
"""

import math

def test_fn(x):
    return x-1

range_l = 0.5
range_u = 1.5 #0.6 #1.5

# Three ways to signal an exceptional condition

# (1) return error code as distinguished value
def dummy_root_finder(fn, range_lower, range_upper):
    # assume we implement our root finding code here
    # which may or may not find a root in the search range
    if (range_lower <= 1.0 and range_upper >= 1.0):
        root = 1.0
        has_root = True
    else:
        root = 0.0
        has_root = False        
    if (has_root):
        return root
    else:
        return math.nan

print("dummy_root_finder:")
r1 = dummy_root_finder(test_fn, range_l, range_u)
if math.isnan(r1):
    print("root not found: rerun probe")
else: 
    print("root=",r1)    
    
# (2) return error code as an additional value
def dummy_root_finder2(fn, range_lower, range_upper):
    # assume we implement our root finding code here
    # which may or may not find a root in the search range
    if (range_lower <= 1.0 and range_upper >= 1.0):
        root = 1.0
        has_root = True
    else:
        root = 0.0
        has_root = False        
    if (has_root):
        return (root, True)
    else:
        return (root, False)

print("dummy_root_finder2:")
r2 = dummy_root_finder2(test_fn, range_l, range_u)
if not r2[1]:
    print("root not found: rerun probe")
else: 
    print("root=",r2[0])    


# (3) throw exception
class my_exception(Exception):
    pass

def dummy_root_finder3(fn, range_lower, range_upper):
    # assume we implement our root finding code here
    # which may or may not find a root in the search range
    if (range_lower <= 1.0 and range_upper >= 1.0):
        root = 1.0
        has_root = True
    else:
        root = 0.0
        has_root = False        
    if (has_root):
        return root
    else:
        raise my_exception()

print("dummy_root_finder3:")
try:
    r3 = dummy_root_finder3(test_fn, range_l, range_u)
except my_exception:
    print("root not found: rerun probe")
else:
    print("root=",r3)    
    





import numpy as np
from numpy import linalg as LA

# take inverse of a singular (non-invertible) matrix
inv_result = LA.inv(np.identity(2))
#inv_result = LA.inv(np.zeros((2,2)))

# by default, if exception is not caught the code stops 
# and prints a traceback so we can see where in the call tree 
# the exception was thrown

# Note that the numpy inv() function can't simply have a 
# precondition of requiring a singular function to be passed in 
# as calling the inv() functiom is the best way to check that 
# the matrix is numerically invertible 
# (even a slightly non-zero determinant may or may not be invertible)

try:
    result = LA.inv(np.identity(2))
  #  LA.inv(np.zeros((2,2)))
except np.linalg.LinAlgError as err:
    # all linear algebra exceptions
    if 'Singular matrix' in str(err):
        # additional info on the particular exceptional
        # condition can be stored in the exception object.
        # Our error handling block:
        # We might run code appropriate for the case where 
        # the matrix is singular e.g. try a more robust but slower matrix 
        # inversion routine here. 
        # Here, as a non-realistic example, we simply flag it with Nans
        result = np.full((2, 2), np.nan)
    else:
        raise
        # otherwise, if we don't handle all the possible 
        # numerical exceptions then rethrow the exception so calling 
        # functions have a chance to handle them
         
print(result)