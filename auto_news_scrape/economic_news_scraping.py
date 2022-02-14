import requests
import random
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"}
url = "https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=101"
res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

news_title = soup.find_all("a", attrs = {"class" : "cluster_text_headline nclicks(cls_eco.clsart)"})
ran_num = random.randint(0,len(news_title)-1)
before_num = -1

print("매일 5개 경제 신문 읽기\n")
print("-----오늘 할당 신문-----\n")

for i in range(5) : 
    while(ran_num == before_num):
        ran_num = random.randint(1,len(news_title))
    print("{0}번째 신문 : {1}\n".format(i+1, news_title[ran_num]['href']))
    before_num = ran_num

