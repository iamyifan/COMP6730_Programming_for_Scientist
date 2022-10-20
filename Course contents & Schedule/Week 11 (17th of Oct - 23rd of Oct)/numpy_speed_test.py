#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 09:33:10 2022

@author: brianparker
"""

import timeit

import numpy

"""
Sum the numbers from 0 to n-1 in different ways.
"""

def for_loop(n=100_000_000):
    s = 0
    for i in range(n):
        s += i
    return s


def sum_numpy(n=100_000_000):
    return numpy.sum(numpy.arange(n, dtype=numpy.int64))


def main():
    print('for pure\t\t', timeit.timeit(for_loop, number=1))
    print('numpy sum\t\t', timeit.timeit(sum_numpy, number=1))


if __name__ == '__main__':
    main()