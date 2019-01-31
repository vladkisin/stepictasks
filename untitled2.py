# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 22:52:58 2019

@author: Lenovo
"""
import requests
from simplecrypt import decrypt, DecryptionException
code = requests.get('https://stepic.org/media/attachments/lesson/24466/encrypted.bin').content
passes = requests.get('https://stepic.org/media/attachments/lesson/24466/passwords.txt').content
 
for p in passes.split():
    try:
        s = decrypt(p, code)
    except DecryptionException:
        pass
    else:
        print(p, s)