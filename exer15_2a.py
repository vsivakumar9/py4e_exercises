# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 17:03:29 2018

@author: Shiva
"""

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

domain=list()
pieces=list()


fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'
#if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    #print(pieces)
    if len(pieces) >=2 :
        domain=pieces[1].split('@') 
        #print(domain)
        orgin=domain[1]
        print(orgin)
        cur.execute('SELECT count FROM Counts WHERE org = ? ', (orgin,))
        row = cur.fetchone()
        #orgdomain2.append(domain[1])
        if row is None:
            cur.execute('''INSERT INTO Counts (org, count)
                    VALUES (?, 1)''', (orgin,))
        else:
            cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                        (orgin,))
            
        conn.commit()

#conn.commit()

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 20'
for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
    
    


        