import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

#serviceurl='http://py4e-data.dr-chuck.net/comments_42.xml?'
serviceurl='http://py4e-data.dr-chuck.net/comments_66995.xml?'

while True:
    address1 = input('Enter location: ')
    if len(address1) < 1: break

    #url = serviceurl + urllib.parse.urlencode({'address': address1})
    url=serviceurl
    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read()
    print('Retrieved', len(data), 'characters')
    #print(data.decode())
    tree = ET.fromstring(data)

    counts = tree.findall('.//count')
    counts = tree.findall('comments/comment')
    print('Count:', len(counts))
    #print(counts)
    countlst=list()
    for item in counts :
        countlst.append( int(item.find('count').text) )
        
    #print(countlst)
    print('Sum:',sum(countlst))