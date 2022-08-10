# -*- coding: utf-8 -*-

import argparse


def odd(n):
    return 2 * n - 1



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-n')
    args = parser.parse_args()
    
    print(odd(int(args.n)))
