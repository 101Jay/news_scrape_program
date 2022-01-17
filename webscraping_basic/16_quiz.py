# 부동산 매물 정보 스크래핑 프로그램

from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")

browser = webdriver.Chrome(options=options)
browser.maximize_window() 

url = 'https://realty.daum.net/home/apt/map'
browser.get(url)
search = browser.find_element_by_xpath('//*[@id="__next"]/div[2]/div/div/div/div[2]/div[1]/div[1]/div/div[1]/input')
search.send_keys("검암역로열파크씨티푸르지오1단지")

time.sleep(1) # 바로 클릭하니 안되서 대기 시간 만들어놓음
browser.find_element_by_class_name("btn-search").click()
time.sleep(1)

num = 2 # xpath 고려
text_list = []
for i in range(0,5):
    mini_list = []
    text_path = browser.find_element_by_xpath('//*[@id="__next"]/div[2]/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[4]/div/div/div[1]/div[2]/div/div[6]/div[{0}]'.format(num))
    text = text_path.find_elements_by_class_name("css-1563yu1")
    for i in range(0,4):
        mini_list.append(text[i].text)
    # print(f"{text[0].text}   {text[1].text}   {text[2].text}   {text[3].text}")
    num += 1 
    text_list.append(mini_list)

browser.quit() # 전체 종료

# 출력 

for idx, text in enumerate(text_list):
    print("="*11, "매물 {0}".format(idx+1), "="*11)
    print("공급/전용(m^2) : {0}m^2\n분양/총세대 : {1}\n분양가 : {2}만원\n1순위 경쟁률 : {3}".format(\
        text[0],text[1],text[2],text[3]))