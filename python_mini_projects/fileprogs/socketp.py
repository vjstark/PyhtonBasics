#socket programming using TCP Protocol..server side
from socket import *

server_name='192.168.1.100'
server_port = 23456

ssocket = socket(AF_INET,SOCK_STREAM)
ssocket.bind((server_name,server_port))
ssocket.listen(1)
print("server ready")

csocket, add = ssocket.accept()
print('connected to',add)
org = csocket.recv(1024).decode()
while org:
	print('received from client',org)
	mod = org.upper()
	print('sent to client',mod)
	csocket.send(mod.encode())
	org = csocket.recv(1024).decode()

csocket.close()
ssocket.close()