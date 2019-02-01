# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 13:46:54 2019

@author: Lenovo
"""


import re
pat = r"https.*html"
while True:
    line = str(input()).rstrip()
    if line == '':
        break
    res = re.findall(pat, line)
    if res:
        print(line)
    