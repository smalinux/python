from bs4 import BeautifulSoup
import requests

imdb_to_250_movies = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
req = requests.get(imdb_to_250_movies)
soup = BeautifulSoup(req.text, "lxml")

c = 1
x = soup.find_all('td', class_='titleColumn')

for i in x:
    print(f"{c}. {i.a.string} {i.span.string}")
    c += 1
