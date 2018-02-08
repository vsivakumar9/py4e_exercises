# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 11:43:34 2018

@author: Shiva
"""

import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect('vsktrackdb.sqlite')
cur = conn.cursor()

#Create needed tables
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;
DROP TABLE IF EXISTS Genre;
                 
CREATE TABLE Artist (
    id      INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id         INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title      TEXT UNIQUE
);

CREATE TABLE Genre (
    id      INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Track (
    id          INTEGER NOT NULL PRIMARY KEY 
                AUTOINCREMENT UNIQUE,
    title       TEXT  UNIQUE,
    album_id    INTEGER,
    genre_id    INTEGER,
    len         INTEGER, 
    rating      INTEGER, 
    count       INTEGER
);
               
''')

#Input xml file 
fname = input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'Library.xml'

#<key>Track ID</key><integer>369</integer> - Track Id3 rd level of dict
#<key>Name</key><string>Another One Bites The Dust</string> - Track name
#<key>Artist</key><string> Queen</string>- Artist
#<key>Album</key><string>Greatest Hits</string> - Album
#<key>Genre</key><string>Rock</string> - Genre
#<key>Total Time</key><integer>217103</integer> - length
#<key>Rating</key><integer>100</integer> - Rating
#<key>Play Count</key><integer>55</integer> - count

def lookup(d, key):
    found = False
    for child in d:
        #print(child)    
        if found : return child.text
        if child.tag == 'key' and child.text == key :
            found = True
    return None

#Parse xml file
xmlstuff = ET.parse(fname)
alldata = xmlstuff.findall('dict/dict/dict')
print('Dict count:', len(alldata))
#print(alldata)


for entry in alldata :
    if ( lookup(entry,'Track ID') is None ) :continue

    name    = lookup(entry, 'Name')
    artist  = lookup(entry, 'Artist')
    album   = lookup(entry, 'Album')
    genre   = lookup(entry, 'Genre')
    length  = lookup(entry, 'Total Time')    
    rating  = lookup(entry, 'Rating')    
    count   = lookup(entry, 'Play Count')    
    
    if name is None or artist is None or album is None or genre is None :
        #print('name or artist or album or genre is None')
        continue

    print(name, artist, album, genre, length, rating , count)
    
    cur.execute('''INSERT OR IGNORE INTO Artist (name) 
        VALUES ( ? )''', ( artist, ) )
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
    artist_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
        VALUES ( ?, ? )''', ( album, artist_id ) )
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Genre (name)
        VALUES( ? )''', ( genre,) )
    cur.execute('SELECT id FROM Genre where name = ? ', (genre, ))
    genre_id = cur.fetchone()[0]
    
    cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, genre_id, len, rating, count) 
        VALUES ( ?, ?, ?, ?, ?, ? )''', 
        ( name, album_id, genre_id, length, rating, count ) )

    conn.commit()
    
#end of python code
    



