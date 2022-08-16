# -*- coding: utf-8 -*-

# Exercise 1(c)

def median(a, b, c):
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    print("median of {}: {}".format([a, b, c], b))
    return b


median(2, 1, 3)
