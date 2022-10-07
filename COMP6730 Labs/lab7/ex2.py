#!/usr/bin/env python
# coding=utf-8

def make_list_of_lists(n):
    the_list = []
    sublist = []
    while n > 0:
        the_list.append(sublist[:])
        sublist.append(len(sublist) + 1)
        n = n - 1
    return the_list


print(make_list_of_lists(5))


def make_list_of_lists2(n):
    the_list = []
    sublist = []
    for i in range(1, n + 1):
        the_list.extend([sublist[:]])
        sublist.insert(len(sublist), i)
    return the_list


print(make_list_of_lists2(5))
