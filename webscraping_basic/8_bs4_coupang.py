import requests
import re
from bs4 import BeautifulSoup
from requests.api import head

# 5페이지까지 가져오기
for i in range(1,6) :
    url = "https://www.coupang.com/np/search?q=%EA%B1%B4%EC%A1%B0%EA%B8%B0&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={0}&rocketAll=false&searchIndexingToken=&backgroundColor=".format(i)
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"}
    res = requests.get(url, headers=headers)
    res.raise_for_status() # 200이 아니면 에러나도록
    soup = BeautifulSoup(res.text, "lxml")

    items = soup.find_all("li", attrs={"class" : re.compile("^search-product")}) # search-product로 시작하는 문자열인지 확인

    lst = []
    for item in items :
        name = item.find("div", attrs={"class" : "name"}).get_text()
        price = item.find("strong", attrs={"class" : "price-value"}).get_text()
        rate = item.find("em", attrs={"class" : "rating"})
        pro_url = item.find("a", attrs = {"class" : "search-product-link"})["href"]
        if rate : 
            rate = rate.get_text()
        else :
            rate = "평점 없음"
            continue
        rate_num = item.find("span", attrs={"class" : "rating-total-count"})
        if rate_num : 
            rate_num = rate_num.get_text()
            rate_num = rate_num.lstrip("(") # rate_num[1:-1] 이런식으로 해줘도 됨
            rate_num = rate_num.rstrip(")")
        else :
            rate_num = "평점 수 없음"
            continue

        # 리뷰 500개 이상, 평점 4.5 이상 되는 것만 조회
        if int(rate_num) >= 500 and float(rate) >=4.5:
            print("제품명 : {0}\n가격 : {1}원\n평점 : {2}점\n평점 수 : {3}개\nURL : {4}".format(name, price, rate, rate_num, "https://www.coupang.com" + pro_url))
        
