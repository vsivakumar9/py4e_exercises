# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 14:32:29 2018

@author: Shiva
"""

import sqlite3

conn=sqlite3.connect('mboxdb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

orgdomain=list()
orgdomain2=list()
pieces=list()
countsdict=dict()

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox-short.txt'
#if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    #print(pieces)
    if len(pieces) >=2 :
        domain=pieces[1].split('@') 
        print(domain)
        orgdomain2.append(domain[1])
        
for item in orgdomain2 :
    countsdict[item] = countsdict.get(item,0) + 1
print(countsdict)

for k,v in countsdict.items() :
    print(k,v)
#    cur.execute('''INSERT INTO Counts (org, count)
#                VALUES (?, 1)''', countsdict(k,v))
    
    


        