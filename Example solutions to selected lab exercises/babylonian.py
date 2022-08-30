
## Exercise 3 in Lab 3: The babylonian algorithm for computing
## square roots.

## The function below has some commented print statements (marked
## with ## TRACE PRINT). If you want to get a better idea of what
## is happening when the algorithm runs, uncomment these and look
## at what is printed.

def square_root(number):
    '''Calculate the square root of number using the babylonian
    algorithm. Number must be positive.'''
    # The initial guess can be anything, but we should get quicker
    # convergence if it's somewhere between the number and zero;
    # we'll use half the number here:
    guess = number / 2
    #print("initial guess:", guess) ## TRACE PRINT
    #print("initial guess squared:", guess ** 2) ## TRACE PRINT
    #print("initial difference:", math.fabs(guess ** 2 - number)) ## TRACE PRINT
    # We want to repeat the loop until the difference between
    # the guess squared and the number is small enough; in other
    # words, repeat while the difference is greater than the
    # threshold:
    while math.fabs(guess ** 2 - number) > 1e-12:
        # Calculate the new guess:
        guess = (guess + (number / guess)) / 2
        #print("new guess:", guess) ## TRACE PRINT
        #print("new guess squared:", guess ** 2) ## TRACE PRINT
        #print("new difference:", math.fabs(guess ** 2 - number)) ## TRACE PRINT
    # The loop ends when the current guess is close enough, so we
    # just return it as the answer:
    return guess

import math

def test_square_root():
    '''Run babylonian square root algorithm and sqrt function from
    math module on some test cases and print the result.'''
    for number in range(1,17):
        b_root = square_root(number)
        m_root = math.sqrt(number)
        print("number =", number,
              "babylonian =", b_root,
              "math.sqrt =", m_root)
