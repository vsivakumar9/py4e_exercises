# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 13:18:49 2018

@author: Shiva
"""

# Use words.txt as the file name
# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

sum=0.0
count=0

for line in fh:
    if line.startswith("X-DSPAM-Confidence:") : 
#       X-DSPAM-Confidence:
        print(line)
        count=count+1
        possp1  = line.find(':')
        poslen1 = len(line)
        sum=sum + float(line[possp1+1:poslen1+1])
        print(sum)
        print(count)
        
print('Average spam confidence:', (sum/count))
print("Done")
