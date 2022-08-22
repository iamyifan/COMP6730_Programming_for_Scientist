#!/usr/bin/env python3
# -*- coding: utf-8 -*-


    
def longest_repeated_substring(s):
    ''' find the longest string that is repeated in s
    Assume s is a string
    '''
    longest = ''
    
    for start in range(0,len(s)):
        for end in range(start+1,len(s)+1):
            sub = s[start:end]
            # check if sub occurs later in s
            if sub in s[start+1:]:
                print(sub, ' is repeated')
                if len(sub) > len(longest):
                    longest = sub
                
    return longest

# this is a litle exercise for you. Send me
# the solution and I will post the best solution(s)
# to the lecture website with proper credit
def all_longest_repeated_substring(s):
    '''
        return a list of all longest repeated substrings in s
        Assume: s is a string
    '''
    return []
