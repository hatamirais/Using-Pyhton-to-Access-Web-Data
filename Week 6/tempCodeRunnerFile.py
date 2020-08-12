import urllib.request, urllib.parse, urllib.error
import json

#Api
api = 'http://py4e-data.dr-chuck.net/json?'

#Input data
url = input('Enter location: ')
url = api + urllib.parse.urlencode({'address':url})
print('Retrieving', url)

page = urllib.request.urlopen(url).read().decode()
print('Retrieved', len(page), 'characters')

try:
    js = json.loads(page)
except:
    js = None

placeId = js['results'][0]['place_id']
print('Place id', placeId)