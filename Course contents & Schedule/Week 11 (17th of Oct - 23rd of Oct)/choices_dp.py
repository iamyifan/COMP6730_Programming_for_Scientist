#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def choices(n, k):
    if k == n or k == 0:
        return 1
    else:
        return choices(n - 1, k) + choices(n - 1, k - 1)

def choices_dp(n, k):
    
    C = [ [0] * (n+1) for i in range(k+1) ]
    
    # base cases
    for j in range(n+1):
        C[0][j] = 1
        
    for i in range(k+1):
        C[i][i] = 1
        
    #print(C)
    #print('\n'.join([ str(row) for row in C]))
    
    for i in range(1,k+1):
        for j in range(i+1,n+1):
            C[i][j] = C[i][j-1] + C[i-1][j-1]

    #print("after filling out:")            
    #print('\n'.join([ str(row) for row in C]))
            
    return C[k][n]

ans = choices_dp(5,3)

