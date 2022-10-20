#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Brute=force exponential time algorithm
def align(s, t, w_gap = 1, w_sub = 1):
    """
    	Align two sequences s and t with gap cost 
	w_gap and substitution cost w_sub
	Returns the edit distance between 2 sequences
    """
    if len(s) == 0:
        return len(t) * w_gap 
    elif len(t) == 0:
        return len(s) * w_gap 
    else:
        if s[-1] == t[-1]:
            d1 = align(s[:-1], t[:-1])
        else:
            d1 = align(s[:-1], t[:-1]) + w_sub
        d2 = align(s, t[:-1]) + w_gap
        d3 = align(s[:-1], t) + w_gap 
        return min(d1, d2, d3)

# Dynamic programming solution
def align_dp(s, t, w_gap, w_sub):
    
    n = len(s)
    m = len(t)
    
    dist = [ [0] * (m+1) for i in range(n+1)]

    # base case top row
    for j in range(m+1):
        dist[0][j] = j
        
    # base case left most column
    for i in range(n+1):
        dist[i][0] = i

    for i in range(1, n+1):
        for j in range(1, m+1):
            # substitution
            if s[i-1] == t[j-1]:
                d1 = dist[i-1][j-1]
            else:
                d1 = dist[i-1][j-1] + w_sub
                
            d2 = dist[i-1][j] + w_gap
            d3 = dist[i][j-1] + w_gap
            dist[i][j] = min(d1, d2, d3)

    
    print('\n'.join([ str(row) for row in dist]))    
    
    return dist[n][m]
    
dist = align_dp("GAATTCA", "GGATCGA", 1, 1)