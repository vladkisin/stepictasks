# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 13:04:15 2019

@author: Lenov
"""

import sys
import re
pat = r'(cat).*(cat)'
for line in sys.stdin:
    line = line.rstrip()
    res = re.findall(pat, line)
    if res:
        print(line)
