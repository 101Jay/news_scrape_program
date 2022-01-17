import requests
from bs4 import BeautifulSoup

year = 2021
# 최근 5년, 5위까지 가져오기
for i in range(0,5):
    url = "https://search.daum.net/search?w=tot&q={0}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR".format(year)
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    images = soup.find_all("img", attrs={"class":"thumb_img"})

    for idx, image in enumerate(images) :
        image_url = image["src"]
        game_image = requests.get(image_url)
        game_image.raise_for_status()

        with open("{0}년 {1}위 영화.jpg".format(year, idx+1), "wb") as f: # 이미지니까 wb로 열기
            f.write(game_image.content) # 이미지 받아오기

        if idx >= 4 : # 5위까지 영화만 받아오기
            break
    year -= 1