# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 19:27:36 2019

@author: Lenovo
"""

def mean(lis):
    return(sum(lis)/len(lis))
math = 0
phys = 0
rus = 0
l = 0
out=[]
data = open(r'C:\Users\Lenovo\dataset_3363_4.txt','r')
line = data.readline()
while line != '':
    s = line.split(';')
    out.append(mean([int(s[1]),int(s[2]),int(s[3])]))
    math += int(s[1])
    phys += int(s[2])
    rus += int(s[3])
    l += 1
    line = data.readline()
data.close()
dat = open(r'C:\Users\Lenovo\dataset_3363_4.txt','w')
for i in out:
    dat.write(str(i)+'\n')
dat.write(str(math/l) + ' ' + str(phys/l) + ' ' + str(rus/l))
dat.close()
    
