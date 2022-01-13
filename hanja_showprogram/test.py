import time
import os
from selenium import webdriver

### selenuim을 이용한 한자 검색
# chromewebdriver 경로 설정 / 현재 작업 폴더에 드라이버 설치
path = os.path.dirname(__file__)
new_path = os.path.join(path,'chromedriver.exe')

driver = webdriver.Chrome(path)

# 다음 한자 사전 이용
url = 'https://small.dic.daum.net/index.do?dic=hanja'

driver.get(url)
time.sleep(2) # 접속할 때까지 잠시 대기

# 검색창 클릭
driver.find_element_by_id("q").click() 

# 한자 입력
element = driver.find_element_by_id("q") 
element.send_keys('幣')

# 입력 후 검색 클릭
driver.find_element_by_id('daumBtnSearch').click() 

# 검색 결과 가져오기
detail_text = driver.find_element_by_class_name('sub_read').text


# list = [1,2,3,4]
# str_list='hi\n'


# if str_list[2] == '\n':
#     print("hi")