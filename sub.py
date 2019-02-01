# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 14:24:32 2019

@author: Lenovo
"""

import re
pat = r'[hH]uman'
while True:
    line = str(input()).rstrip()
    if line == '':
        break
    res = re.sub(pat, 'computer', line)
    print(res)
    