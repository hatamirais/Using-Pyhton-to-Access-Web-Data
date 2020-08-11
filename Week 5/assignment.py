import xml.etree.ElementTree as ET
from urllib.request import urlopen
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')

total_number = 0
sum = 0

#Retriving how many character are in the xml
print('Retriving ', url)
xml_file = urlopen(url, context=ctx).read()
print('Retrived', len(xml_file), 'characters')

#stuff is the tree of xml
stuff = ET.fromstring(xml_file)
#XPath selector string to look through the entire tree of XML for any tag named 'count'
counts = stuff.findall('.//count')
for count in counts:
    sum += int(count.text)
    total_number += 1

print('Count: ', total_number)
print('Sum: ', sum)