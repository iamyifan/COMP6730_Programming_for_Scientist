#!/usr/bin/env python
# coding=utf-8

def allbut(a_list, index):
    return a_list[:index] + a_list[index+1:]


my_list = [1, 2, 3, 4]
my_short_list = allbut(my_list, 2)
print(my_short_list)
print(my_list)
