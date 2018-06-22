import socket
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

try:
	cities = ['Mumbai','Delhi','Chennai','Bengaluru']
	tmp = []
	socket.create_connection(('www.google.com',80))
	for i in cities:
		api_address = 'https://api.openweathermap.org/data/2.5/weather?units=metric'+'&q='+i+'&appid=a7649e94312e5486d0d09ed8a7996837'
		res1 = requests.get(api_address)
		#print(res1)
		wdata = requests.get(api_address).json()
		#print(wdata)
		temp = wdata['main']['temp']
		tmp.append(temp)

	plt.bar(cities,tmp,width=0.25,label='temperature')

	plt.xlabel("cities")
	plt.ylabel("temperature")
	plt.show()
	#msg = 'You are in the city '+city+'and the weather is '+str(temp)
	#print(msg)
except OSError:
	print('check network')