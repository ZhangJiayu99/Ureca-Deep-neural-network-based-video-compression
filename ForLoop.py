#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 11:45:49 2018

@author: zhangjiayu
"""

words = ['cat', 'window', 'apple']

for i in words:
    print(i, len(i))
    
for i in range(5):
    print(i)
    
for i in range(len(words)):
    print(words[i])
    
    
#following codes is going to find prime numbers
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n/x)
            break
    else:
        print(n, 'is a prime number')
        
        

    
    