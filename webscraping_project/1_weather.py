import requests
from bs4 import BeautifulSoup

# if__name__ == "__main__": 을 이용하여 각 파일 모두 함수로 정의하고 쓸 수도 있음

url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%9D%B8%EC%B2%9C+%EB%82%A0%EC%94%A8'
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

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
print(info[0][4],",",info[0][0],info[0][1],info[0][2])
print("현재 {0} (최저 {1} / 최고 {2})".format(info[1][5:], info[2][4:], info[3][4:]))
print("오전 강수확률 {0} / 오후 강수확률 {1}".format(info[4], info[5]))
print(info[6]+"\n"+info[7])