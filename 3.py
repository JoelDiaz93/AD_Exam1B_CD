import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

def find_2nd(string, substring):
    return string.find(substring, string.find(substring) + 1)


def find_1st(string, substring):
    return string.find(substring, string.find(substring))


response = requests.get("https://www.elcomercio.com/tag/juegos-olimpicos/")
soup = BeautifulSoup(response.content)

Contenidos = []
ListSearch = []

titulos = soup.find_all("h3")
contenido = soup.find_all("p")

'''post_course=soup.find_all("span", class_="text-1 weight-semi line-tight")
post_provider=soup.find_all("a", class_="color-charcoal italic")'''

extracted = []
for element in contenido:
    # print(element)
    element = str(element)
    limpio = str(element[find_1st(element, '>') + 1:find_2nd(element, '<')])

    # print(limpio)
    ListSearch.append({"Content": limpio.strip()})

CLIENT = MongoClient("mongodb://localhost:27017/")
try:
    CLIENT.admin.command('ismaster')
    print('MongoDB connection: Success')
except ConnectionFailure as cf:
    print('MongoDB connection: failed', cf)
db = CLIENT["python"]
game = db["juegosolimpicos"]

x = game.insert_many(ListSearch)
