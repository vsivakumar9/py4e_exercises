# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 13:18:49 2018

@author: Shiva
"""

# Use words.txt as the file name
fname = input("Enter file name: ")
try :
    fh = open(fname)
except:
    print ('invalid file name',fname)
    quit()
    
count=0
for line in fh:
    #fh.read()
    count=count+1
    lineup = line.upper()
    #print(lineup)
    #print('count of rec:',count)
    lineup1 = lineup.rstrip()
    print(lineup1)