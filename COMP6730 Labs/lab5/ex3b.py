#!/usr/bin/env python
# coding=utf-8


def count(seq, P):
    ''' Count the number of element of type P.
    
    Attributes:
        seq: any iterable object
        P: the type of elements to be counted

    Returns:
        count(int): the number of elements of type P
    '''
    count = 0
    for elem in seq:
        if type(elem) == P:
            count += 1
    return count


if __name__ == '__main__':
    seq = ['a', 'b', 1, 2, 3]
    P = str
    print(count(seq, P))

