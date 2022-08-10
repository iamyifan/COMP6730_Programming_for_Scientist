# -*- coding:utf-8 -*-

import argparse


def determinant(m):
    a, b = m[0][0], m[0][1]
    c, d = m[1][0], m[1][1]
    return ad - bc


def carmer(m, c):
    m1 = [[c[0], m[0][1]], [c[1], m[1][1]]]
    x = determinant(m1) / determinant(m)
    m2 = [[m[0][0], c[0]], [m[1][0], c[1]]]
    y = determinant(m2) / determinant(m)
    return x, y


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', type=list)
    parser.add_argument('-c', type=list)
    args = parser.parse_args()
    print(carmer(args.m, args.c))

