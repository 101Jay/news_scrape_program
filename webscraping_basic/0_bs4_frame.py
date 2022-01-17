import requests
from bs4 import BeautifulSoup

url = ''
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
