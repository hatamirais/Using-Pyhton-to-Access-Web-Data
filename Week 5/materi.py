#from xml1.py

import xml.etree.ElementTree as ET

data = '''
<person>
    <name> Chuck </name>
    <phone type='intl'>
        +1 734 303 4456
    </phone>
    <email hide='Yes'/>
</person>
'''

tree = ET.fromstring(data) #I can change tree to something else
print('Name: ', tree.find('name').text)
#find name tag and grab the text
print('Attr: ', tree.find('email').get('hide'))
#find email, grab the attribute and get the tag hide
