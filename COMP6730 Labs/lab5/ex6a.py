#!/usr/bin/env python
# coding=utf-8


def count_repetitions(string, substring):
    '''
    Count the number of repetitions of substring in string. Both
    arguments must be strings.
    '''
    n_rep = 0
    # p is the next position in the string where the substring starts
    p = string.find(substring)
    # str.find returns -1 if the substring is not found
    while p >= 0:
        n_rep = n_rep + 1
        # find next position where the substring starts
        # p = string[p + 1:len(string) - p].find(substring)
        offset = string[p + 1:len(string)].find(substring)
        if offset == -1:
            break
        p += offset + 1
    return n_rep


if __name__ == '__main__':
    # if string == 'aaa' and substring == 'a'
    # the function will go into infinite loop
    string = input()  
    substring = input()
    res = count_repetitions(string, substring)
    print(res)
