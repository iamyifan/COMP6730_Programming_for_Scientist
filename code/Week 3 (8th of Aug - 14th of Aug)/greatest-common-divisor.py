#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def gcd(a, b):
    ''' find the greatest common divisor of a, b
    assumptions: a >= b > 0    '''
    while a % b != 0:
        r = a % b
        a = b
        b = r
    
    return b
