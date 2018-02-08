# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 13:39:51 2018

@author: Shiva
"""

fname = input("Enter file:")
if len(fname) < 1 : fname = "mbox-short.txt"
fhandle = open(fname)
linelist=list()
hourlist1=list()
hourlist2=list()
countsdict=dict()

for line in fhandle :
    if line.startswith('From ') :
        linelist=line.split()
        if len(linelist) >= 6 :
            hourlist1=linelist[5].split(':')
            hourlist2.append(hourlist1[0])

for hour in hourlist2 :
    countsdict[hour]=countsdict.get(hour,0) + 1
    
for k1,v1 in sorted(countsdict.items()) :
    print(k1,v1)

