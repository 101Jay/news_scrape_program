import requests
from bs4 import BeautifulSoup

# https://comic.naver.com/genre/bestChallenge?&page=1

for page in range(1,71):
    url = r"https://comic.naver.com/genre/bestChallenge" + "?&page={0}".format(page)
    res = requests.get(url)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "lxml")

    best_challenge_webtoon = soup.find_all("h6", attrs={"class":"challengeTitle"})

    with open("베스트 도전 만화 리스트.txt", "a", encoding="utf-8") as file:
        for webtoon in best_challenge_webtoon:
            # print(webtoon.get_text().strip())
            file.write(webtoon.get_text().strip())
            file.write("\n")

# url = "https://comic.naver.com/genre/bestChallenge"