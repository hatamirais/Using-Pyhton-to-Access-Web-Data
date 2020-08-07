import re

name = input('Enter file:')

handle = open(name)

#create empty list of number
number = []
total = 0

for line in handle:
    line = line.rstrip()
    #find number start from 0-9 
    y = re.findall( '[0-9]+', line)
    #add found number to the empty list
    number = number + y

#adding total number found
for n in number:
    total = total + int(n)

print(("Total = "), total)