# -*- coding: utf-8 -*-

# Exercise 3: The square root algorithm

def babylonian_algorithm(a, x, diff=10e-6):
    # a: the number to solve
    # x: the initial guess
    while abs(x**2 - a) > diff:
        x = (x + a / x) / 2 
    print("the square root of {} is {}".format(a, x))
    return x


babylonian_algorithm(1000, 10)
