# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 14:44:43 2019

@author: Lenovo
"""

import sys
import re
pat = r'\b[aA]+\b'
for line in sys.stdin:
    res = re.sub(pat, 'argh', line, count =1)
    if res:
        print(res, end = '')
    else: 
        print(line, end = '')