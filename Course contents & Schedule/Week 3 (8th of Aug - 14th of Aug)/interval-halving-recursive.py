
# Example from Lecture 1 in week 3: The recursive interval-halving
# algorithm for solving an equation.

import math

def area(r):
    '''Returns the area of a circle with radius r;
    r must be a non-negative number.'''
    return math.pi * (r ** 2)

def solve(f, y, lower, upper):
    '''Recursive implementation of the interval-halving algorithm
    for finding a solution to f(x) ~= y.'''
    print("lower:", lower, "upper:", upper)
    middle = (lower + upper) / 2
    if math.fabs(f(middle) - y) < 1e-5:
        return middle
    else:
        if f(middle) < y:
            return solve(f, y, middle, upper)
        else:
            return solve(f, y, lower, middle)

# Apply the algorithm to find r such that area(r) == 1 (approx).
# solve must be called with a starting interval that contains a
# solution; otherwise the recursion will not stop.
print("the answer is:", solve(area, 1, 0.5, 0.6))
