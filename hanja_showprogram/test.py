import time
from selenium import webdriver

# <input type="text" name="query" id="ac_input" title="검색어 입력" value="" 
# accesskey="s" autocomplete="off" autocapitalize="off" autocorrect="off" maxlength="55" 
# class="keyword" tabindex="0" data-value="">

'''
<button onclick="clickcr(this, 'sch.go','','',event); return false;" class="btn_search" title="검색">검색</button>
'''

path = r'C:\Users\jsKim\Desktop\PythonWorkspace\chromedriver.exe'
driver = webdriver.Chrome(path)
url = 'https://hanja.dict.naver.com/#/main'

driver.get(url)
time.sleep(2)

driver.find_element_by_class_name("btn_close my_btn_close").click()
driver.find_element_by_id("ac_input").click()
element = driver.find_element_by_id("ac_input")
element.send_keys('伯')
driver.find_element_by_xpath('//*[@id="searchArea"]/div/button').click()