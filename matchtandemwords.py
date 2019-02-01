# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 14:01:50 2019

@author: Lenovo
"""

import sys
import re
pat = r'\b(\w+)\1\b'
for line in sys.stdin:
    line = line.rstrip()
    res = re.findall(pat, line)
    if res:
        print(line)