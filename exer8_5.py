# -*- coding: utf-8 -*-
"""
#Created on Thu Jan 18 19:19:31 2018
#8.5 Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end.
#Hint: make sure not to include the lines that start with 'From:'.
@author: Shiva
"""

fname = input("Enter file name: ")
#if len(fname) < 1 : 
#   fname = "mbox-short.txt"

fh = open(fname)
print('fh', fh)
count1 = 0
count2 = 0 
wordlist=list()

for line1 in fh :
    count1=count1+1
    if line1.startswith('From ') :
        #print(line1)
        wordlist = line1.split() 
        print(wordlist)
        if len(wordlist) >= 2 :
            const=wordlist[0]
            print (const)
            #if  wordlist[0] == 'From'
            count2=count2+1
            print(wordlist)
            print(wordlist[1])
            print(count1)
            print(count2)
            
    
    
    
