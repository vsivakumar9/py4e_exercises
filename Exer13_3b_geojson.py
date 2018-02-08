# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 18:00:00 2018

@author: Shiva
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 16:44:31 2018

@author: Shiva
"""

import urllib.request, urllib.parse, urllib.error
import json

#api_key = False
api_key = True

# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
#serviceurlnew=http://geocoding-backend.googleapis.com
api_key = 'AIzaSyBlz5AApM06TFq7kQEUkuC1o2k2-Z6Q_2s'

if api_key is False:
    serviceurl = "http://py4e-data.dr-chuck.net/geojson?"
else :
    serviceurl = "https://maps.googleapis.com/maps/api/place/textsearch/json?"

#serviceurl = 'http://py4e-data.dr-chuck.net/geojson?'
#addr1='South Federal University'
addr1='Politecnico di Milano'

while True :
    addr1 = input('Enter location: ')
    if len(addr1) < 2 : break

    #parms = dict()
    #parms["query"] = address
    #if api_key is not False: parms['key'] = api_key
    #url = serviceurl + urllib.parse.urlencode(parms)


    # open url and get json data
    #url = serviceurl + urllib.parse.urlencode({'address': addr1})
    url = serviceurl + urllib.parse.urlencode({'address': addr1,'key':api_key})
    print('Retrieving',url)
    uh  = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retreived',len(data),'characters')
    
    try:
        js= json.loads(data)
    
    except:
        js=None
        
    if not js or 'status' not in js or js['status'] != 'OK' :
        print('==== Failure To Retrieve ====')
        print(data)
        continue
    
    print(json.dumps(js,indent=4))
    print(len(js))
    
    placeid=js["results"][0]["place_id"]
    
    print(placeid)
    
    
    
    