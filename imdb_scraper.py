# import libraries
import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from time import sleep
from random import randint

# Initialize storage
titles = []
years = []
time = []
imdb_ratings = []
metascores = []
votes = []
us_gross = []

# Accept only English titles
headers = {"Accept-Language": "en-US, en;q=0.5"}

pages = np.arange(1,1001,50)
for page in pages:
  page = requests.get("https://www.imdb.com/search/title/?groups=top_1000&start="+str(page) + "&ref_=adv_nxt", headers=headers)
  soup = BeautifulSoup(page.text, "html.parser")
  movie_div = soup.find_all('div',class_="lister-item mode-advanced")

  sleep(randint(2,10))
  for container in movie_div:
    name = container.h3.a.text
    titles.append(name)

    year = container.h3.find('span',class_='lister-item-year').text
    years.append(year)

    runtime = container.find('span',class_='runtime').text if container.p.find('span', class_='runtime') else ''
    time.append(runtime)

    imdb = float(container.strong.text)
    imdb_ratings.append(imdb)

    metascore = container.find('span',class_='metascore').text if container.find('span', class_='metascore') else '-'
    metascores.append(metascore)

    nv = container.find_all('span', attrs={'name': 'nv'})
    vote = nv[0].text
    votes.append(vote)
    grosses = nv[1].text if len(nv) > 1 else '-'
    us_gross.append(grosses)

movies = pd.DataFrame({
  'movie': titles,
  'year' : years,
  'runtime': time,
  'imdb': imdb_ratings,
  'metascore': metascores,
  'votes': votes,
  'us_gross_millions': us_gross,
})

movies['year'] = movies['year'].str.extract('(\d+)').astype(int)
movies['runtime'] = movies['runtime'].str.extract('(\d+)').astype(int)
movies['metascore'] = movies['metascore'].str.extract('(\d+)')
movies['metascore'] = pd.to_numeric(movies['metascore'], errors='coerce')
movies['votes'] = movies['votes'].str.replace(',','').astype(int)
movies['us_gross_millions'] = movies['us_gross_millions'].map(lambda x: x.lstrip('$').rstrip('M'))
movies['us_gross_millions'] = pd.to_numeric(movies['us_gross_millions'], errors='coerce')

print(movies.dtypes)
print(movies)

movies.to_csv('movies.csv')