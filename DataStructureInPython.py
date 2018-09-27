#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 15:21:57 2018

@author: zhangjiayu
"""

# example of list:
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print fruits.count('apple')
print fruits.index('banana')
print fruits.index('banana', 4)  # Find next banana starting a position 4
fruits.reverse()
print fruits
fruits.append('grape')
print fruits
fruits.sort()
print fruits
print fruits.pop()
del fruits[0]
print fruits






#example of tuples:
#Note that tuples are immutable
t = 12345, 54321, 'hello!'
# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)


#example of dictionary:
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print tel
print tel['jack']
del tel['sape']
tel['irv'] = 4127
print list(tel)
sorted(tel)
print tel
print ('guido' in tel)







