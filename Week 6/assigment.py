import urllib.request, urllib.parse, urllib.error
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

total_number = 0
sum = 0

while True:

    url_page = input('Enter location: ')
    if len(url_page) < 1:
        break
    print('Retrieving', url_page)

    url = urllib.request.urlopen(url_page).read().decode()
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