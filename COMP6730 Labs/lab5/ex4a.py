#!/usr/bin/env python
# coding=utf-8


my_string = "Angry Public Swamp Methods"

L = len(my_string)

print(my_string[1:L])

print(my_string[0:L - 1])

print(my_string[0:L:2])

print(my_string[L:0:-1])

print(my_string[6:6 + 6])

print(my_string[11:11 - 6:-1])

# print(my_string[2*L])  # IndexError

print(my_string[0:2*L])

