import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/index"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# print(soup.title)
# print(soup.title.get_title()) # text만 가져옴
# print(soup.a) # soup에 있는 내용 중 가장 먼저 나온 a element 내용 가져옴 
# print(soup.a.attrs) # a태그에 있는 속성들 보여줌
# print(soup.a["href"]) # a element의 href 속성 가져옴

# HTML 내용을 잘 모를 때
# print(soup.find("h4", attrs={"class" : "Ntxt_new_best"})) # a element 중 class가 Ntxt_new_best인 첫 번째 element 출력

rank1 = soup.find("li", attrs={"class":"rank01"})

# print(rank1.a) # rank1로 받아 온 것 중에 a만 출력(자식으로 내려감)
# print(rank1.a.get_text())

# 형제로 li로 넘어가기
# print(rank1.next_sibling.next_sibling.a.get_text()) # 형제 사이에 개행이 있을 때는 두 번 해주면 된다. 
# rank1.find_next_sibling("li") # 그게 싫다면 find_next_sibling을 이용해도 된다. 
# find_next_siblings("li") 하면 형제들 모두 가져옴

# rank2 = rank1.next_sibling.next_sibling
# rank1 = rank2.previous_sibling.previous_sibling # next가 있으면 previous도 있다 이전 형제로 간다.

# print(rank1.parent) # 부모로도 올라갈 수 있다.

webtoon = soup.find("a", text = "전지적 독자 시점") # 속성을 통해 찾을 수도 있다.
print(webtoon)

