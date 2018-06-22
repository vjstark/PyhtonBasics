import socket
import requests

try:
	socket.create_connection(('www.google.com',80))
	res = requests.get('https://ipinfo.io/')
	print(res)
	data = res.json()
	print(data)
	city = data['city']
	print(city)
except OSError:
	print('check network')