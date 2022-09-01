#!/usr/bin/env python
# coding=utf-8


def count_capitals(s):
    count = 0
    for c in s:
        if ord('A') <= ord(c) <= ord('Z'):
            count += 1
    return count


if __name__ == '__main__':
    print(count_capitals('aLKSzxcvm,ASD'))
