import time
from selenium import webdriver

browser = webdriver.Chrome() # "./chromedriver.exe"  같은 디렉토리 안에 있어서 생략 가능

# 페이지 접속
browser.get("http://naver.com")

# 로그인 버튼 클릭
browser.find_element_by_class_name("link_login").click()

# id, password 입력
browser.find_element_by_id("id").send_keys("your_ID")
browser.find_element_by_id("pw").send_keys("your_password")

# 로그인 버튼 클릭
browser.find_element_by_id("log.login").click()
time.sleep(3)

# id 지우고 다시 입력
browser.find_element_by_id("id").clear()
browser.find_element_by_id("id").send_keys("again_your_ID")

# html 정보 출력
print(browser.page_source)

# 브라우저 종료
# browser.close() -> 현재 탭만 종료
browser.quit() # 전체 브라우저 종료

