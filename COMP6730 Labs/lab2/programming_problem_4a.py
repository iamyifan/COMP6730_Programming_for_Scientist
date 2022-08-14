# -*- coding: utf-8 -*-

import argparse

# the price of a book is $24.95
# online book seller offering a 40% discount
# shipping cost is $3 for the first copy
# $0.75 for each additional copy


def total_price(n):
    assert n > 0

    book_price = 24.95
    discount = 0.4
    first_shipping_price = 3
    additional_shipping_price = 0.75
    
    n_books_price = n * book_price * (1 - discount)
    n_shipping_price = first_shipping_price + (n - 1) * additional_shipping_price
    total_price = n_books_price + n_shipping_price
    return total_price


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n')
    args = parser.parse_args()
    
    res = total_price(int(args.n))
    print("total price:", res)


