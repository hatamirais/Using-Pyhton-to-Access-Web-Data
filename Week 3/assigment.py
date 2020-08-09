import requests as req

response = req.get('http://data.pr4e.org/intro-short.txt')

print(response.text)

#More in here http://zetcode.com/python/requests/