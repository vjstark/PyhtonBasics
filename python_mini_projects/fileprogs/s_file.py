from socket import *

server_name = '127.0.0.1'
server_port = 25411

#make a socket
ssocket = socket(AF_INET,SOCK_STREAM)
#bind
ssocket.bind((server_name,server_port))
#listen
ssocket.listen(1)
print('server ready')
#accept
csocket, add = ssocket.accept()
#receive filename from server and check validity
#if found send prompt asking to download
fn = csocket.recv(1024).decode()
import os
found = False
if os.path.isfile(fn):
	found = True
else:
	found = False
csocket.send(str(found).encode())
##received ip from client..send packets.
ans = csocket.recv(1024).decode()
if ans == 'y':
	f.open(fn,'rb')
	fd = f.read(1024)
	while fd:
		csocket.send(fd)
		fd = f.read(1024)
		while fd:
			csocket.send(fd)
			fd = f.read(1024)

#close connections
csocket.close()
ssocket.close()
