# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 11:01:41 2019

@author: Lenovo
"""
def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k
import csv
counter = {}
with open('Crimes.csv') as f:
    file = csv.reader(f)
    for row in file:
        if row[5] in counter.keys():
            counter[row[5]] += 1
        else:
            counter[row[5]] = 0
print(get_key(counter, max(counter.values())))