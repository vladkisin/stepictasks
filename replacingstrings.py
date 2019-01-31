# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 15:27:48 2019

@author: Lenovo
"""
s = str(input())
a = str(input())
b = str(input())
count = 0
for i in range(1001):
    if a in s:
        s = s.replace(a,b)
        count += 1
    else:
        break
print(count) if count <= 1000 else print('Impossible')