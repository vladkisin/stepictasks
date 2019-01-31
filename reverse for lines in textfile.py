# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 18:57:03 2019

@author: Lenovo
"""
lines=[]
with open('dataset_24465_4.txt', 'r+') as f:
    for line in f:
        lines.append(line.strip())
lines = lines[-1::-1]
with open('dataset_24465_4.txt', 'w') as f:
    f.write('\n'.join(lines))
#for i in range(len(lines)-1, -1, -1):
   # f.write(lines[i])
