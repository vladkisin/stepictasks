# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 19:56:37 2019

@author: Lenovo
"""

from bs4 import BeautifulSoup
import requests
import re 
output = []
good = set()
url = str(input())
temp = r'\w+(\.\w+\-?)+'
page = requests.get(url)
page = page.text
soup = BeautifulSoup(page, features = 'html.parser')
for link in soup.find_all('a'):
    output.append(link.get('href'))
output = set(output)
for item in output:
    item = str(item)
    if '-2' in item:
        good.add('www.m-2.ru')
    else:
        res = re.search(temp, item)
        if res:
            good.add(res.group(0))
good = sorted(list(good))
for site in good:
    print(site)