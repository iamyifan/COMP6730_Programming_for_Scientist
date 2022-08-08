
# Example from Lectures 1 and 2 in week 3: The interval-halving
# algorithm for solving an equation (both recursive and iterative
# versions).

import math

def solve_recursive(f, y, lower, upper):
    '''
    Recursive implementation of the interval-halving algorithm
    for finding a solution to f(x) = y (approximately).
    Assumptions: f is function of one argument, it is increasing
    on the interval [lower, upper] and there is a solution f(x) = y
    somewhere in this interval.
    '''
    # Find the mid-point of the interval:
    middle = (lower + upper) / 2
    # Base case: if f(middle) is close enough to y, we have our solution
    if math.fabs(f(middle) - y) < 1e-6:
        return middle
    else:
        # Otherwise, if f(middle) is < y, the solution must lie
        # in the interval [middle, upper],
        if f(middle) < y:
            return solve_recursive(f, y, middle, upper)
        else:
        # else, (i.e., if f(middle) is > y), the solution must lie
        # in the interval [lower, middle]
            return solve_recursive(f, y, lower, middle)

def solve_iterative(f, y, lower, upper):
    '''
    Iterative implementation of the interval-halving algorithm
    for finding a solution to f(x) = y (approximately).
    Assumptions: f is function of one argument, it is increasing
    on the interval [lower, upper] and there is a solution f(x) = y
    somewhere in this interval.
    '''
    middle = (lower + upper) / 2
    while math.fabs(f(middle) - y) >= 1e-6:
        ## uncomment the print call to see what is happening in each
        ## iteration of the loop.
        # print("lower:", lower, "upper:", upper)
        if f(middle) < y:
            lower = middle
        else:
            upper = middle
        # recompute the mid-point since at least one interval end
        # has changed:
        middle = (lower + upper) / 2
    return middle

def area(r):
    '''Returns the area of a circle with radius r;
    r must be a non-negative number.'''
    return (r ** 2) * math.pi

# Apply the algorithm to find r such that area(r) == 1 (approx).
# solve must be called with a starting interval that contains a
# solution; otherwise the recursion or loop will not stop.
print("Answer (computed recursively):", solve_recursive(area, 1, 0.5, 0.6))
print("Answer (computed iteratively):", solve_iterative(area, 1, 0.5, 0.6))
