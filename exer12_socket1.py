# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 14:39:53 2018

@author: Shiva
"""

import socket

mysock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysock.connect( ('data.pr4e.org',80) )
cmd='GET http://data.pr4e.org/remeo.txt HTTP/1,0\n\n'.encode()
mysock.send(cmd)

while True :
    data=mysock.recv(512)
    if (len(data)) < 1 :
        break
    print (data.decode())
    
mysock.close()
