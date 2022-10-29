#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 10:20:25 2022

@author: brianparker
"""

# These code examples highlight some aspects of the interaction
# of functions and variables that may be surprising to beginning programmers.
# These same concepts apply to most other languages too.
# Try stepping through the code in spyder.

#################################################
# Issue 1: pass-by-value on function calling
#################################################

# This function modifies its formal parameter c in the function body.
def f(c):
    c = c * 2
    return c

b = 1  # Here we define a global variable
f(b)   # We pass b to the function as its actual argument.

print(b) # Was b updated to 2 by f?  

# Ans: no the global variable b is not modified, despite the passed-in argument
# being modified to 2 in the function f. 
# This is because python functions use "pass-by-value" by default, so a *copy*
# of b is assigned to the formal parameter c when the function is called.
# (This is the usual behaviour we would expect for a function in mathematics).
# Note: for large variables this copy could be inefficient and we will see 
# later in the course that python uses a different form of argument passing for
# "large" variables.

    
#################################################
# Issue 2: Use of execution stack for nested function calls
#################################################
    
# Functions can, and typically do, call other functions in their implementation.
# For each nested function call, a copy of the local variables and formal parameters of 
# the higher level function needs to be temporarily stored while the 
# called function executes. When the called function returns its local variables and 
# formal parameters will be discarded and the callings function's variables reinstated.
# This is implemented in the computer hardware as an exectution stack, which is 
# a LIFO (last-in first-out) data structure. 
# See https://en.wikipedia.org/wiki/Stack_(abstract_data_type)     
   
# deg_to_rad function is called by sin_of_deg 
import math
def deg_to_rad(y):
    print("deg_to_rad stack frame:")
    print("y =",y)
 #   assert(False)    # We have added an assert here which causes an error
    return y * math.pi / 180

def sin_of_deg(x):
    print("sin_of_deg stack frame:")
    print("x =",x)
    x_in_rad = deg_to_rad(x)
    print("sin_of_deg stack frame:")
    print("x_in_rad =",x_in_rad)
    return math.sin(x_in_rad)

# Calculate sin_of_degree, which calls deg_to_rad
answer = sin_of_deg(23)   

# We have added print statments here as a simple, but very useful, form of debugging.
# Run this code to see the variables saved on the stack for each function call,
# as described in the lecture notes.
# Later we will see how to use a debugger to more easily examine the execution stack 
# of our code. 

# After running the code, remove the comment from the line with the assert.
# We will cover assertions, which are useful in debugging our code,
# later in the course. In this case the assertion causes an error to occur.
# Look at the traceback produced by python and make sure you understand the 
# calling sequence of the functions.

#################################################
# Issue 3: Scope of variable names
#################################################

c = 0

def g(a):
    c = a * 2
    return c

g(1)
print(c)

# In this function g, we assign c to twice the argument.
# Does c refer to the global variable c, or does it refer to the newly created
# local variable?
# Ans: a new local variable is created on the stack when the function is called,
# as we saw in the previous example,
# and inside the function "c" refers to this local variable on the stack. It
# does not refer to the global variable c. 
# We say that the name "c" has local or function scope in lines 89-91 as there
# it refers to the local variable, and we say "c" has global scope elsewhere in the
# source code.
# The reason most modern languages use similar scoping rules is that it 
# ensures that functions are self-contained: if all variables had global scope
# then a change in the name of a local variable in a function could change the
# meaning of the entire code by accidentally modifing a global variable.

# Note, if we really did want to change the global variable c, we could write:
c = 0

def g(a):
    global c 
    c = a * 2
    return c

g(1)    
print(c)

# There is an example of this in robot.py. Note that it is generally poor 
# programming style for a function to have the side-effect of modifying global 
# state, unless it is essential as in the robot example, as it is more difficult
# to understand and debug.
    
