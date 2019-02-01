# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 14:50:40 2019

@author: Lenovo
"""
import sys
import re
pat1 = r'\b(\w)(\w)'
for line in sys.stdin:
    word = re.sub(pat1, r'\2\1', line)
    print(word, end = '')