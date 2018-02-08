# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 13:36:57 2018

@author: Shiva
"""

import re

fname=input('Input file name: ')
fhand=open(fname)

numlist=list()

for line in fhand :
    strnum=re.findall('([0-9]+)',line)
    print(strnum)
    print(line)
        
    if len(strnum) >= 1 :
        for word in strnum :
            num=int(word)
            print(num)
            numlist.append(num)
            print(numlist)
            
print (len(numlist))
print('sum of sumlist: ' , sum(numlist))
