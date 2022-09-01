#!/usr/bin/env python
# coding=utf-8


def ceasar_cipher(string, shift):
    if shift >= 0:
        shift %= 26 
    else:
        shift = -(abs(shift) % 26)
    
    if shift == 0: 
        return string

    res = ""
    for i in range(len(string)):
        if not string[i].isalpha():
            res += string[i]
            continue
        res += chr(ord(string[i]) + shift)

    return res


if __name__ == '__main__':
    print(ceasar_cipher("Et tu, Brutus!", 3))
    print(ceasar_cipher("IBM", -1))
