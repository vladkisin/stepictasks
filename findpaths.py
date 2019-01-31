# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 14:12:58 2019

@author: Lenovo
"""
with open ('ans.txt', 'w') as answer:
    import os
    import os.path
    ans = []
    for cur_dir, dirs, files in os.walk('main'):
        for file in files:
            if '.py' in file:
                answer.write(cur_dir+'\n')
                break

    
            