# -*- coding: utf-8 -*-

# Exercise 1: Programs with conditional branching
# Exercise 1(a)

def print_grade(mark):
    if mark >= 80:
        print("High Distinction")
    else:
        if mark >= 70:
            print("Distinction")
        else:
            if mark >= 60:
                print("Credit")
            else:
                if mark >= 50:
                    print("Pass")
                else:
                    print("Fail")



print_grade(45)
