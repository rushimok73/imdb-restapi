import requests
import re
from bs4 import BeautifulSoup
import json

def scraperfn():
    res = []
    response = requests.get('https://www.imdb.com/chart/top?ref_=nv_mv_250')
    soup = BeautifulSoup(response.text,'html.parser')
    movies = soup.find_all(class_= "lister-list")[0].find_all('tr')
    for item in movies:
        data = {}
        poster = item.find(class_ = "posterColumn").find('img')['src']
        title = item.find(class_ = "titleColumn").get_text()
        rating = item.find(class_ = "ratingColumn imdbRating").get_text()
        date = title[-6:-2]
        title = re.sub(r"[\n\t]*", "", title)
        rating = re.sub(r"[\n]*", "", rating)
        date = re.sub(r"[\n]*", "", date)
        title = title[10:-6].strip()
        data['moviename'] = title
        data['movierating'] = rating
        data['movieyear'] = date
        data['movieimage'] = poster
        res.append(data)
    return res
