# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 16:49:05 2019

@author: Lenovo
"""
def find_children(root,dic = {},i=0):
    for child in root:
        dic[child.attrib['color']] += i+2
    i += 1
    try:
        find_children(root[i-1], i=i, dic = dic) 
    except:
        return dic
from xml.etree import ElementTree
xml = input()
root = ElementTree.fromstring(xml)
dic = {'red': 0, 'green': 0, 'blue' : 0}
find_children(root, dic)
dic[root.attrib['color']] += 1
print(str(dic['red']) + ' ' + str(dic['green']) + ' ' + str(dic['blue']))