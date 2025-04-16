import requests
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup
import os
print("Chemin actuel:", os.getcwd())

with open("annexe_py/index.html", "r") as file:
    soup = BeautifulSoup(file.read(), 'html.parser')
    print(soup.find_all("p"))