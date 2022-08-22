# -*- coding: utf-8 -*-

# Exercise 4: Digit Sums

def sum_odd_digits(number):
    num_str = str(number)
    sum_odds = 0
    for num in num_str:
        if int(num) % 2 == 0:
            continue
        sum_odds += int(num)
    print("sum of odds: {}".format(sum_odds))
    return sum_odds

def sum_even_digits(number):
    num_str = str(number)
    sum_evens = 0
    for num in num_str:
        if int(num) % 2 == 1:
            continue
        sum_evens += int(num)
    print("sum of evens: {}".format(sum_evens))
    return sum_evens

def sum_all_digits(number):
    total_sum = sum_odd_digits(number) + sum_even_digits(number)
    print("for {}, the total sum of digits is {}".format(number, total_sum))


sum_all_digits(1234)
