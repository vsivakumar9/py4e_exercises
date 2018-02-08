# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 13:16:32 2018

@author: Shiva
"""

import urllib.request, urllib.parse, urllib.error
import json

#serviceurl='http://py4e-data.dr-chuck.net/comments_42.json'
#serviceurl='http://py4e-data.dr-chuck.net/comments_66996.json'

while True:
    serviceurl = input('Enter location: ')
    if len(serviceurl) < 1: break

    #url = serviceurl + urllib.parse.urlencode({'address': address1})
    url=serviceurl
    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read()
    print('Retrieved', len(data), 'characters')
    #print(data.decode())
    
    js = json.loads(data)
    #print('count:', len(js))
    
    cntlist=list()
    for item in js["comments"] :
        cnt =  int(item["count"])
        cntlist.append(cnt)
    
    #print(cntlist)
    print(sum(cntlist))
    
    #print(js["comments"][1]["count"])