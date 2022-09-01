#!/usr/bin/env python
# coding=utf-8


my_list = [i + 1 for i in range(26)]

L = len(my_list)

print(my_list[1:L])

print(my_list[0:L - 1])

print(my_list[0:L:2])

print(my_list[L:0:-1])

print(my_list[6:6 + 6])

print(my_list[11:11 - 6:-1])

# print(my_list[2*L])  # IndexError

print(my_list[0:2*L])

