
import math

def derivative(f, x, d):
    '''Calculate an approximation of the derivative of
    function f at point x, using a straight line of
    width 2 * d.
    f must be a function with one parameter, and x a
    numeric value.
    The approximation tends towards the true value of
    the derivative as d tends to zero; however, for
    values of d close to zero, the error caused by the
    limited precision of floating point numbers also
    increases.'''
    return (f(x + d) - f(x - d)) / (2 * d)

print("the derivative of sin(x) at pi/4 is:",
      derivative(math.sin, math.pi/4, 0.01))

def square(x):
    return x ** 2

print("the derivative of x squared at 2 is:",
      derivative(square, 2, 0.001))
