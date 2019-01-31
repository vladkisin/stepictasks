# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 15:48:49 2019

@author: Lenovo
"""

s = str(input())
t = str(input())
counter = 0
for i in range(len(s)-len(t)+1):
    check = s[0+i:len(t)+i]
    if t in check:
        counter += 1 
print(counter)
