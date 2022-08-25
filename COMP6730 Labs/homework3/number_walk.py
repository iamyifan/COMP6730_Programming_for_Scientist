## COMP1730/6730 S2 2022 - Homework 3
# Submission is due 09:00am, Monday the 29th of August, 2022.

## YOUR ANU ID: u7351505
## YOUR NAME: Yifan Luo

## You should implement two functions number_to_string(m,n) and
## string_to_number(s). The `pass` statements are only a placeholder 
## which you should replace with your implementation. The first function,
## number_to_string(m,n) must return a string representing the rational
## number m/n; the second function, string_to_number(s), must return a pair
## of mutally prime positive integers m and n in a form of two-tuple (m,n)

def number_to_string(m, n):
    """
    Compute the path towards the number on the binary tree
    for a rational number given by the pair of (m, n).

    Parameters:
        m (int): the first element of the input rational number, numerator
        n (int): the second element of the input rational number, denominator

    Returns:
        s (str): the path representing the rational number m/n
    """

    assert type(m) == type(n) == int, "m and n must be integers"
    assert m > 0 and n > 0, "m and n must be positive"
    s = ''
    while m != n:
        if m < n:  # if m < n, set n to be n - m and add L to s
            n -= m
            s += "L"
        else:  # if m > n, set m to be m - n and add R to s
            m -= n
            s += "R"
    return s


def string_to_number(s):
    """
    Compute the pair of positive mutually prime integers (m, n)
    which is represented on the binary tree by the string-path s,
    consisting of symbols L and R only.

    Parameters:
        s (str): the string-path which consists of only characters 'L' and 'R'

    Returns:
        (m, n) (tuple(int, int)): the pair of positive mutually prime integers
        which is represented on the binary tree by the string-path s
    """

    assert type(s) == str, "s must be a string"
    # assert s    # check s only consists of L and R

    # three pointers trick:
    # left, mid and right pointer initialize with 0/1, 1/1 and 1/0
    left, mid, right = (0, 1), (1, 1), (1, 0)
    # start from the top of the binary tree,
    # iterate each letter ("L" or "R") to update the returned tuple
    for direction in s:
        if direction == "L":  # if the next step towards left
            right = mid       # shift the right pointer to the position of mid pointer
            mid = (mid[0] + left[0], mid[1] + left[1])    # update the value of mid pointer
        else:                 # if the next step towards right
            left = mid        # shift the left pointer to the position of mid pointer
            mid = (mid[0] + right[0], mid[1] + right[1])  # update the value of mid pointer
    return mid

def test_number_number_to_string():
    '''
    This function runs a number of tests of the number_to_string function.
    If it works ok, you will just see the output ("all tests passed") at
    the end when you call this function; if some test fails, there will
    be an error message.
    '''
    assert number_to_string(1, 1) == ''
    assert type(number_to_string(1, 1)) == str
    assert number_to_string(2, 1) == 'R'
    assert type(number_to_string(2, 1)) == str
    assert number_to_string(3, 1) == 'RR'
    assert type(number_to_string(3, 1)) == str
    assert number_to_string(4, 1) == 'R' * 3
    assert type(number_to_string(1, 4)) == str
    assert number_to_string(3, 11) == 'LLLRL'
    assert type(number_to_string(89, 55)) == str
    assert number_to_string(89, 55) == 'RLRLRLRLR'
    assert type(number_to_string(8, 111)) == str
    assert number_to_string(144, 89) == 'RL' * 5
    print("all tests passed")


def test_string_to_number():
    '''
    This function runs a number of tests of the string_to_number function.
    If it works ok, you will just see the output ("all tests passed") at
    the end when you call this function; if some test fails, there will
    be an error message.
    '''
    assert string_to_number('') == (1, 1)
    assert type(string_to_number('')) == tuple
    assert string_to_number('L') == (1, 2)
    assert type(string_to_number('R')) == tuple
    assert string_to_number('LR') == (2, 3)
    assert type(string_to_number('RL')) == tuple
    assert string_to_number('RL' * 5) == (144, 89)
    assert type(string_to_number('LR' * 10)) == tuple
    assert string_to_number('LLLLLLLLLLL') == (1, 12)
    assert string_to_number('RRRRRRRRRR') == (11, 1)
    print("all tests passed")
