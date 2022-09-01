#!/usr/bin/env python
# coding=utf-8


def remove_substring_everywhere(string, substring):
    '''
    Remove all occurrences of substring from string, and return
    the resulting string. Both arguments must be strings.
    '''
    p = string.find(substring)
    lsub = len(substring) # length of the substring
    while p >= 0:
        # string[p : len(string) - lsub] = string[p + lsub : len(string)]
        # string = string[:p] + string[p + lsub:len(string)]
        string = string.replace(substring, '')
        p = string.find(substring)
    return string


if __name__ == '__main__':
    string = input()
    substring = input()
    res = remove_substring_everywhere(string, substring)
    print(res)
