#socket programming using TCP Protocol..client side
from socket import *

server_name = '192.168.1.101'
server_port = 23456

csocket = socket(AF_INET,SOCK_STREAM)
print('connecting to server...')
csocket.connect((server_name,server_port))
print('connected to server')

data = input('Enter data to send to server. press q to quit')
while data != 'q':
	print('sending data to server')
	csocket.send(data.encode())
	mdata = csocket.recv(1024).decode()
	print('received data from server',mdata)
	data = input()

csocket.close()
print('connection closed')