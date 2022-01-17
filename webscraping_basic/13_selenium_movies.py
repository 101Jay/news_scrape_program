from attr import attr, attrs
import requests
from bs4 import BeautifulSoup

# 참고 -> 드라이버가 btn-search 뜰 때까지만 대기하게 하기
# from selenium.webdriver.support import expected_conditions as EC
# elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME,"btn-search")))

url = "https://play.google.com/store/movies"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
"Accept-Language":"ko-KR,ko"}


res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")

# with open("test.html","w",encoding="utf8") as file:
#     file.write(soup.prettify())

movies = soup.find_all("div", attrs={"class":"ULeU3b neq64b"})

for movie in movies:
    title = movie.find("div", attrs={"class" : "Epkrse"}).get_text()
    print(title)