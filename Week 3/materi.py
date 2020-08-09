'''
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect( ('data.pr4e.org', 80) )
'''

#An HTTP Request in Python

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode() #this in UTF-8 byte
mysock.send(cmd)

while True:
    data = mysock.recv(512) #get 512 character
    if (len(data) < 1): #if the data is less then 1 remember len is for what
        break
    print(data.decode())
mysock.close()