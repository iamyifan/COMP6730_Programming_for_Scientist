#!/usr/bin/env python
# coding=utf-8

x = 27

def increment_x():
    global x
    print("x before increment:", x)
    # y = x + 1
    x = x + 1 # local variable 'x' referrenced before assignment 
    print("x after increment:", x)
    locals().items()
    print(locals().items())
    print(globals().items())


increment_x()

print("(global) x after function:", x)
