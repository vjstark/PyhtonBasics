from bs4 import BeautifulSoup
import requests
import datetime

res = requests.get('https://www.brainyquote.com/quote_of_the_day.html')
print(res)

soup = BeautifulSoup(res.text,'lxml')
quote = soup.find('img',{"class":"p-qotd"})
#print(quote)
print(quote['alt']) #text
#print(quote['src']) #image
link = quote['src']
link = 'https://www.brainyquote.com/quote_of_the_day'+str(link) #image path in website
filename = datetime.datetime.now().date()

r = requests.get(link)
with open(str(filename) + str(1) + '.jpg','wb') as f:
	f.write(r.content)