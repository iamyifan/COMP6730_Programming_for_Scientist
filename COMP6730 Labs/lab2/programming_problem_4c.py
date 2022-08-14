# -*- coding:utf-8 -*-

import argparse


def solve1(a, b):
    return b / a


def solve2(a1, b1, c1, a2, b2, c2):
    r = a1 / a2
    y = (c1 - r * c2) / (b1 - r * b2)
    x = (c1 - b1 * y) / a1
    return x, y

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-a')
    parser.add_argument('-b')
    parser.add_argument('-a1')
    parser.add_argument('-b1')
    parser.add_argument('-c1')
    parser.add_argument('-a2')
    parser.add_argument('-b2')
    parser.add_argument('-c2')
    args = parser.parse_args()

    if args.a and args.b:
        print(solve1(int(args.a), int(args.b)))

    if args.a1 and args.b1 and args.c1 and args.a2 and args.b2 and args.c2:
        print(solve2(int(args.a1), int(args.b1), int(args.c1), int(args.a2), int(args.b2), int(args.c2)))

