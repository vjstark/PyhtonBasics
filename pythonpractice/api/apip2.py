import socket
import requests
try:
	city='Mumbai'
	socket.create_connection(('www.google.com',80))
	api_address = 'https://api.openweathermap.org/data/2.5/weather?units=metric'+'&q='+city+'&appid=a7649e94312e5486d0d09ed8a7996837'
	res1 = requests.get(api_address)
	print(res1)
	wdata = requests.get(api_address).json()
	print(wdata)
	temp = wdata['main']['temp']
	msg = 'You are in the city '+city+' and the weather is '+str(temp) +' degree celsius.'
	print(msg)
except OSError:
	print('check network')