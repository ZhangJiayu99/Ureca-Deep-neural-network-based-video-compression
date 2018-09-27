#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 14:54:23 2018

@author: zhangjiayu
"""

#To practice define and call functions.
def fib(n):
    '''Print a Fibonacci series up to n.'''
    a, b = 0, 1
    while a < n:
        print a,
        a, b = b, a + b
    print()
        
fib(2000)



#Keywords argument function
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print "-- This parrot wouldn't", action, 
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")
    

parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword

#Note that following cases will be invalid:
#parrot()                     # required argument missing
#parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
#parrot(110, voltage=220)     # duplicate value for the same argument
#parrot(actor='John Cleese')  # unknown keyword argument



# Another function:  *name for tuple; **name for dictionary
# Note that the order in which the keyword arguments are printed is guaranteed
# to match the order in which they were provided in the function call.
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])
    
    
cheeseshop("Limburger", "It's very runny, sir.", 
           "It's really very, VERY runny, sir.", 
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")