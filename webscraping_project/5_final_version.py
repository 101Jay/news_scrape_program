import requests
from bs4 import BeautifulSoup

def create_soup(url):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup

#########################################
# 날씨 정보 출력
url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%9D%B8%EC%B2%9C+%EB%82%A0%EC%94%A8'
soup = create_soup(url)

info = [] # 리스트로 담아서 출력

weat = soup.find("div", attrs={"class" : "weather_info"})

line1 = weat.find("p", attrs={"class" : "summary"}).get_text().strip().split(" ") # ~도 높/낮아요
info.append(line1) # info [0] -> line1 list

info.append(weat.find("div", attrs={"class" : "temperature_text"}).get_text().strip()) # info [1] 현재 온도
info.append(soup.find("span", attrs={"class": "temperature_inner"}).find("span", attrs={"class":"lowest"}).get_text()) # info [2] -> 최저
info.append(soup.find("span", attrs={"class": "temperature_inner"}).find("span", attrs={"class":"highest"}).get_text()) # info [3] -> 최고

info.append(soup.find_all("span", attrs={"class":"rainfall"})[0].get_text()) # 오전 강수확률
info.append(soup.find_all("span", attrs={"class":"rainfall"})[1].get_text()) # 오후 강수확률

mise = soup.find("ul", attrs={"class" : "today_chart_list"}).find_all("li") 
info.append(mise[0].get_text().strip()) # 미세먼지
info.append(mise[1].get_text().strip()) # 초미세먼지

print("[오늘의 날씨]")
print(info[0][4]+",",info[0][0],info[0][1],info[0][2])
print("현재 {0} (최저 {1} / 최고 {2})".format(info[1][5:], info[2][4:], info[3][4:]))
print("오전 강수확률 {0} / 오후 강수확률 {1}".format(info[4], info[5]))
print(info[6]+"\n"+info[7])

#########################################
# 헤드라인 뉴스
url = 'https://news.naver.com/'
soup = create_soup(url)

text = soup.find_all("a", attrs={"class": "cjs_news_a"})

print("\n[헤드라인 뉴스]")
for i in range(0,3):
    print("{}.".format(i+1),text[i].find("div", attrs={"class": "cjs_t"}).get_text())
    print("(링크 : {})".format(text[i]["href"]))

#########################################
# 경제 뉴스
url = 'https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=101'
soup = create_soup(url)

text = soup.find_all("a", attrs={"class": "cluster_text_headline nclicks(cls_eco.clsart)"})

print("\n[경제 뉴스]")
for i in range(0,3):
    print("{}.".format(i+1),text[i].get_text())
    print("(링크 : {})".format(text[i]["href"]))

#########################################
# 영어 지문 가져오기
url = 'https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english#;'
soup = create_soup(url)

text_box = soup.find_all("div", attrs={"class" : "conv_txt"})
eng_text = text_box[1].find_all("span", attrs = {"class" : "conv_sub"})
kor_text = text_box[0].find_all("span", attrs = {"class" : "conv_sub"})

print("\n[오늘의 영어 회화]")
print("(영어 지문)")
for i in eng_text:
    print(i.get_text())
print("\n(한글 지문)")
for i in kor_text:
    print(i.get_text())

# if__name__ == "__main__": 을 이용하여 위에 모두 함수로 정의하고 쓸 수도 있음