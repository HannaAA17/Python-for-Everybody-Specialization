import urllib.request, urllib.parse, urllib.error
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input("Enter URL: ")
    if len(address) < 1: break
    counts = 0
    uh = urllib.request.urlopen(address)
    data = uh.read()
    info = json.loads(data)
    
    print('User count:', len(info["comments"]))
    
    for item in info['comments']:
        print('Name', item['name'])
        print('count', item['count'])
        counts += item['count']
    print(counts)
