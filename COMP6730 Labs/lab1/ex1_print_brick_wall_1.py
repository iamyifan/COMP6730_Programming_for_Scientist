# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 14:40:53 2022

@author: yifan luo
@uid: u7351505
"""

# procedure to print two overlapping brick rows:
# def print_bricks:  # miss "()"
#     print("--+-----+---")
#       print("|     |")  # wrong indent
#     print("-----+-----+")
#          print("|     |")  # wrong indent


# repeat the two rows three times to make a higher wall:
# print_bricks[]  # "[]" -> "()"
# print_bricks()
# print_bricks  # miss "()"


def print_bricks():
    print("--+-----+---\n  |     |\n-----+-----+\n     |     |")


print_bricks()
print_bricks()
print_bricks()
