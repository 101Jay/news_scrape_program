import requests
from bs4 import BeautifulSoup

url = 'https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=101'
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

text = soup.find_all("a", attrs={"class": "cluster_text_headline nclicks(cls_eco.clsart)"})

print("[경제 뉴스]")
for i in range(0,4):
    print("{}.".format(i+1),text[i].get_text())
    print("(링크 : {})".format(text[i]["href"]))
