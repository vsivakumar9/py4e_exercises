# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


cnt=input('Enter Count:')
pos=input('Enter Position:')
ipos=int(pos)
icnt=int(cnt)

#url = input('Enter - ')

#def geturlname(url):
    
urlnew = input('Enter - ')
#urlnew='http://py4e-data.dr-chuck.net/known_by_Fikret.html'
#urlagn='http://py4e-data.dr-chuck.net/known_by_Kaydin.html'
# Repeat process icnt times
print('Retrieving:',urlnew)

for i in range(icnt) :
    #print('icnt:',i)
 
    url=urlnew
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all of the anchor tags
    tags = soup('a')
    
# Find the tag in position ipos
    countpos=0
    for tag in tags:
        #print(tag)
        countpos=countpos+1
        #print('countpos:',countpos)
        urlnew  = tag.get('href', None)
        #print(urlnew)
        if countpos == ipos :
            print('Retrieving:',urlnew)
            break
  
