'''
1. Which of the following best describes "Regular Expressions"?


'''

'''
import re

x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y)
'''

import re

len = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
y = re.findall( '\S+?@\S+')
print(y)