import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

browser = webdriver.Chrome()
browser.maximize_window() # 창 최대화

url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%84%A4%EC%9D%B4%EB%B2%84+%ED%95%AD%EA%B3%B5%EA%B6%8C&oquery=%EB%84%A4%EC%9D%B4%EB%B2%84+%ED%95%AD%EA%B3%B5%EA%B6%8C&tqi=hPRs0dprvhGssZfSYvNssssstP8-335263"
browser.get(url)

# ... why?
browser.find_element_by_link_text("가는날 선택").send_keys(Keys.ENTER)

browser.find_elements_by_link_text("20")[0].click()
browser.find_elements_by_link_text("21")[0].click()

browser.find_element_by_link_text("도착지 선택").click()

browser.find_element_by_xpath('//*[@id="_flight_section"]/div/div[2]/div[2]/div[1]/div[2]/div/div/table[1]/tbody/tr[1]/td[1]/a').click()


browser.find_element_by_link_text("항공권 검색").click()