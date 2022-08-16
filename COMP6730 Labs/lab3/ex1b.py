# -*- coding: utf-8 -*-

# Exercise 1(b)

def print_grade(mark):
    if mark >= 80:
        print("High Distinction")
    elif mark >= 70:
        print("Distinction")
    elif mark >= 60:
        print("Credit")
    elif mark >= 50:
        print("Pass")
    else:
        print("Fail")


print_grade(75)
