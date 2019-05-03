from socket import *

server_name = '127.0.0.1'
server_port = 25411
#socket
csocket = socket(AF_INET,SOCK_STREAM)
print('connecting to server')
#connect
csocket.connect((server_name,server_port))
print('Connected to server')
#take file input and send to server
fn = input('Enter the filename you want to download')
print('sending response to server')
csocket.send(fn.encode())
#received input from server
#prompt to donwload
f = csocket.recv(1024).decode()
print(f,type(f))
if f==True:
	print('File Found')
	ans = input(print(' "y": download,"n": quit'))
	if ans == 'y':
		csocket.send(ans.encode())
		print('response sent to server. downloading file...')
		f = open(fn+'copy','ab')
		fd = csocket.recv(1024)
		while fd:
			f.write(fd)
			fd = csocket.recv(1024)
	else:
		print('closing connection')
		csocket.close()
else:
	print('File not found')
	csocket.close()
