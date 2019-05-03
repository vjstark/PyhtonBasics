import requests
from bs4 import BeautifulSoup

url = 'http://mu.ac.in/portal/distance-open-learning/examination/science/'

res =requests.get(url)
print(res)

soup = BeautifulSoup(res.text,'lxml')

data = []
for para in soup.find_all('a'):
	link = para.get('href')
	if(link.endswith('.pdf')):
		data.append(link)