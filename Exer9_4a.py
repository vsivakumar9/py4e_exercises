# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 14:45:10 2018

@author: Shiva
"""

#Write a program to read through the mbox-short.txt and figure out who has 
#the sent the greatest number of mail messages. The program looks for 'From ' 
#lines and takes the second word of those lines as the person who sent the mail. 
#The program creates a Python dictionary that maps the sender's mail address to 
#a count of the number of times they appear in the file. After the dictionary 
#is produced, the program reads through the dictionary using a maximum loop to 
#find the most prolific committer.

name = input("Enter file: ")
if len(name) < 1 : name = "mbox-short.txt"
fhandle = open(name)
linelist=list()
emailids=list()
countsdict=dict()
for line in fhandle :
    if line.startswith('From ') :
        linelist=line.split()
        if len(linelist) >= 2 :
            emailids.append(linelist[1])

for emailid in emailids :
    countsdict[emailid]=countsdict.get(emailid,0)  + 1
    
Maxcount=None
Maxemailid=None

for emailid1,count in countsdict.items() :
    if Maxcount is None or count > Maxcount:
        Maxcount = count
        Maxemailid = emailid1
        
print(Maxemailid,Maxcount)
    
        