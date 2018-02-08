# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 12:34:15 2018
@author: Shiva
"""

fname = input("Enter file name: ")
fh = open(fname)
lst   = list()
lst1 = list()
count=0
for line in fh :
    lst1=line.split()
    count=count+1
    if count == 1 :
        lst=lst1
        
    print('printing lst1')
    print(lst1)
    print(len(lst1))
    
    print('printing lst')
    print(lst)
    print(len(lst))
    
    for i in range(len(lst1)) :
        print (i)
        if lst1[i]  in lst :
           print(lst1[i])
        else :   
            lst.append(lst1[i])
        print(lst1[i])
    print(lst1) 
    print(lst)
    
lst.sort()
print(lst)

 
#print(line.rstrip())
