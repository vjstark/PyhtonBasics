from bs4 import BeautifulSoup
import requests
import datetime

res = requests.get('https://bingwallpaper.com/')
print(res)

soup = BeautifulSoup(res.text,'lxml')

image_box = soup.find('a',{'class':'cursor_zoom'})
image = image_box.find('img')
#print(quote)
 #text
#print(quote['src']) #image
link = image['src']
filename = datetime.datetime.now().date()

r = requests.get(link)
with open(str(filename) + str(1) + '.jpg','wb') as f:
	f.write(r.content)