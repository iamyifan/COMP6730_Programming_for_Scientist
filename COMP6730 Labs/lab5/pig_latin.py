#!/usr/bin/env python
# coding=utf-8


def pig_lation(word):
    vowels = "aeiou"
    if word[0] in vowels:
        return word + "yay"
    first_vowel = 0
    while first_vowel < len(word):
        if word[first_vowel] in vowels:
            break
        first_vowel += 1
    return word[first_vowel:] + word[:first_vowel] + "ay"
    

if __name__ == "__main__":
   words = ["dog", "scratch", "is", "apple"]
   for word in words:
       print(pig_lation(word))
