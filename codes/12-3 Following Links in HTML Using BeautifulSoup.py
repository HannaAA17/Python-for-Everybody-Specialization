# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
countt = int(input('Enter count: '))
positionn = int(input('Enter position: '))

print(url)

# Retrieve only the link and repeat untill count
while countt>0:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    url = tags[positionn-1].get('href', None)
    print(url)
    #print(tags[positionn-1].contents)
    countt -= 1

# Retrieve all of the anchor tags
#tags = soup('a')
#print(tags[positionn-1].contents)
#print(tags[positionn-1].get('href', None))
#for tag in tags:
    #print(tag.get('href', None))
    #print(tag.contents)

