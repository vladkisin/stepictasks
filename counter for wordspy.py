# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 19:27:36 2019

@author: Lenovo
"""
def get_key(d, valuex):
    for key, value in d.items():
        if value == valuex:
            return key
def counter_in_text(text):
    d={}
    for line in text:   
        s = line.strip().lower().split(' ')
        for i in s:
            if i in d.keys():
                d[i] += 1
            else:
                d[i] = 1
    return str(get_key(d, max(d.values()))) + ' ' + str(max(d.values()))
data = open(r'C:\Users\Lenovo\dataset_3363_3.txt','r')
text = data.readlines()
out = counter_in_text(text)
data.close()
dat = open(r'C:\Users\Lenovo\dataset_3363_3.txt','w')
dat.write(out)
dat.close()