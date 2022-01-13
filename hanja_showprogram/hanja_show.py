import re
import random
import time
import tkinter.messagebox as msgbox
from bs4 import BeautifulSoup
from tkinter import *
from selenium import webdriver


root = Tk()
root.title("3급 한자 랜덤 프로그램")
root.geometry("500x500+3000+100") # 가로 * 세로 + x좌표 + y좌표
root.resizable(False, False)  # 창 가로 / 세로로 늘이기 허용 안 함

kor_text = '가'
chn_text = '痛'

#### function 구현

china_check = re.compile('[一-龥]')
korean_check = re.compile('[가-힣]')

def go_search():
    pass
    # path = 'chromedriver.exe'
    # driver = webdriver.Chrome(path)
    # url = 'https://hanja.dict.naver.com/#/main'

    # driver.get(url)
    # time.sleep(2)

    # driver.find_element_by_id("ac_input").click()
    # element = driver.find_element_by_id("ac_input")
    # element.send_keys(chn_text)
    # driver.find_element_by_xpath('//*[@id="searchArea"]/div/button').click()
    

def go_next():
    global kor_text, chn_text
    # 같은 글자 또 나오지 않게 확인해줘야 함
    origin_text = chn_text
    while True :
        with open("3급한자.txt", "r", encoding="utf-8") as file:
            text_all = file.readlines() # 줄 별로 리스트 만들어짐
            ran_num1 = random.randint(0,len(text_all)-1) # 리스트 크기내에서 랜덤으로 정수 추출
            line = text_all[ran_num1]
            ran_num2 = random.randint(0,len(line)-1) # 문자열 크기내에서 랜덤으로 정수 추출
            word = line[ran_num2]

            # 한국어가 선택되었다면
            if korean_check.match(word):
                kor_text = word
                # 어디까지 그 한글에 해당하는 한자인지 확인
                check_len = 0
                cnt = 1
                while True:
                    check_text = line[ran_num2+cnt]
                    if korean_check.match(check_text):
                        check_len = cnt - 1
                        break
                    cnt += 1

                # 범위 안에서 다시 랜덤 수를 추출하여 한자 지정
                chn_text = line[ran_num2 + random.randint(1,check_len)]

            # 한자가 선택되었다면
            elif china_check.match(word):
                chn_text = word
                cnt = 1
                while True:
                    kor_text = line[ran_num2-cnt]  # IndexError: string index out of range 발생
                    if korean_check.match(kor_text):
                        break
                    cnt += 1

            # 그 외 다른 것이 선택되었다면
            else :
                pass
        if chn_text != origin_text :
            kor_lable.config(text=kor_text)
            chn_lable.config(text=chn_text)
            break



#### layout 구현

## 상단 프레임 -> 정보 등
top_frame = Frame(root)
top_frame.pack(fill='x', expand=True)

top_label = Label(top_frame, text='made by_Jay code')
top_label.pack(side='right',padx=5)


## 글자 프레임
lettter_frame = Frame(root)
lettter_frame.pack(pady=30)

# 1) 왼쪽 프레임 -> 한글 넣기
left_frame = Frame(lettter_frame, relief='solid', borderwidth=5)
left_frame.pack(side='left')

kor_lable = Label(left_frame, text=kor_text ,font=(NONE,100),padx=50,pady=100)
kor_lable.pack()

# 2) 오른쪽 프레임 -> 한자 넣기
right_frame = Frame(lettter_frame, relief='solid', borderwidth=5)
right_frame.pack(side='right')

chn_lable = Label(right_frame, text=chn_text, font=(NONE,100),padx=50,pady=100)
chn_lable.pack()

### 하단 프레임
bottom_frame = Frame(root)
bottom_frame.pack(side = 'bottom')

## 넘어가기용 버튼
btn_next = Button(bottom_frame, text = '다음', width=10, height=2, command=go_next)
btn_next.pack(side='left', pady = 10, padx = 5)

## 검색용 버튼
btn_naver = Button(bottom_frame, text = '검색', width=10, height=2, command=go_search)
btn_naver.pack(side='right', pady=10, padx = 5)


root.mainloop()