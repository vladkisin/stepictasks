# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 16:19:13 2019

@author: Lenovo
"""
import requests
temp = 'http://numbersapi.com/{}/math?json=true'
with open('dataset_24476_3.txt','r') as f, open('numbers.txt','w') as w:
    for line in f:
        line = line.strip()
        r = requests.get(temp.format(line))
        j = r.json()
        if j['found'] == True:
            w.write('Interesting\n')
        else:
            w.write('Boring\n')
        