import requests
from bs4 import BeautifulSoup

from movie import Movie


def getSoup(url):
    result = requests.get(url)
    source = result.text
    soup = BeautifulSoup(source, 'html.parser')
    return soup


def getValues(raw_object, attr, htmlClass):
    values = raw_object.find_all(attr, class_=htmlClass)
    return values


def getValue(raw_object, attr, htmlClass):
    value = raw_object.find(attr, class_=htmlClass)
    return value

# Example Usage
#
# def getMovies(url):
#     soup = getSoup(url)
#     raw_objects = soup.find_all("tr", class_="css-o6sgwe")
#     movies = []
#     for raw_movie in raw_movies:
#         raw_title = getValue(raw_movie, "td", "css-1u7zfla e126mwsw1")
#         title = raw_title.text
#         link = "https://reelgood.com" + raw_title.a.attrs["href"]
#         values = getValues(raw_movie, "td", "css-1u11l3y")
#         releaseYear = values[0].text
#         rating = values[2].text
#         movies.append(Movie(title, releaseYear, rating, link))
#     return movies
