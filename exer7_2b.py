# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 13:18:49 2018

@author: Shiva
"""

# Use words.txt as the file name
# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
numarray=[]
count=0

for line in fh:
    if line.startswith("X-DSPAM-Confidence:") : 
        count=count+1
        print('count:',count)
        possp1  = line.find(':')
        poslen1 = len(line)
        num=float(line[possp1+1:poslen1+1])
        print(count)
        print(line)
        print(num)
        numarray.append(num)
        #avg=sum(numarray)/len(numarray)
        
#print('Average spam confidence:', avg)
print('end')