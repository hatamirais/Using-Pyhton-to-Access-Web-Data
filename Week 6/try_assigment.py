import urllib.request, urllib.parse, urllib.error
import json

#Data collection
link = input('Enter location: ')
print('Retrieving', link)

url = urllib.request.urlopen(link).read().decode()
print('Retrieved', len(url), 'characters')

try:
    js = json.loads(url)
except:
    js = None

cn = 0
sm = 0
for item in js['comments']:
    cn += 1
    sm += int(item['count'])

print('Count:', cn)
print('Sum:', sm)