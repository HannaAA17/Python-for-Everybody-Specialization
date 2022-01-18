import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    summ = 0
    address = input('Enter location: ')
    if len(address) < 1: break

    uh = urllib.request.urlopen(address)

    data = uh.read()
    print('Retrieved', len(data), 'characters')
    
    tree = ET.fromstring(data)
    counts = tree.findall('.//count')
    print("Count:",len(counts))
    for item in counts:
        summ += float(item.text)
    print("Sum:",summ)
