#!/usr/bin/env python
# coding=utf-8

atup = (1, 2, 3, 4)

print(type(atup))

print(atup + atup)

print(atup * 4)

print(atup[0])

print(type(atup[0]))

print(atup[-2])

print(atup[1:-2])

print(atup[1:2])

# btup = "abdc"
btup = (1, 3, 2, 4)

print(atup < btup)

for elem in atup:
    print(elem)

print(min(atup))

print(max(atup))

print(sorted(atup))
