import re
import random
import time
import os
import tkinter.messagebox as msgbox
from bs4 import BeautifulSoup
from tkinter import *
from selenium import webdriver


root = Tk()
root.title("3급 한자 학습 프로그램")
root.geometry("500x500+3000+100") # 가로 * 세로 + x좌표 + y좌표
root.resizable(False, False)  # 창 가로 / 세로로 늘이기 허용 안 함

kor_text = '가'
chn_text = '痛'

#### function 구현

china_check = re.compile('[一-龥]')
korean_check = re.compile('[가-힣]')

def go_search():
    ## selenuim을 이용한 한자 검색
    # chromewebdriver 경로 설정 / 현재 작업 폴더에 드라이버 설치
    cur_path = os.path.dirname(__file__)
    path = os.path.join(cur_path,'chromedriver.exe')

    driver = webdriver.Chrome(path)

    # 다음 한자 사전 이용
    url = 'https://small.dic.daum.net/index.do?dic=hanja'

    driver.get(url)
    time.sleep(2) # 접속할 때까지 잠시 대기

    # 검색창 클릭
    driver.find_element_by_id("q").click() 

    # 한자 입력
    element = driver.find_element_by_id("q") 
    element.send_keys(chn_text)

    # 입력 후 검색 클릭
    driver.find_element_by_id('daumBtnSearch').click() 

    # 검색 결과 가져오기
    detail_text = driver.find_element_by_class_name('sub_read').text
    explain_lable.config(text = detail_text)

    driver.quit()

def go_next():
    # 한자 파일 경로 설정
    cur_path = os.path.dirname(__file__)
    file_path = os.path.join(cur_path,'3급한자.txt')

    global kor_text, chn_text
    origin_text = chn_text # 이전 글자와 중복 확인
    while True :
        with open(file_path, "r", encoding="utf-8") as file:
            text_all = file.readlines() # 줄 별로 리스트 만들어짐
            ran_num1 = random.randint(0,len(text_all)-1) # 리스트 크기내에서 랜덤으로 정수 추출
            line = text_all[ran_num1]
            ran_num2 = random.randint(0,len(line)-1) # 문자열 크기내에서 랜덤으로 정수 추출
            word = line[ran_num2]

            # 한국어가 선택되었다면 -> 뒤로 가면서 그 다음 첫 한글이 나오는 인덱스 확인 후, 그 범위 안에서 다시 랜덤으로 한자 추출
            if korean_check.match(word):
                kor_text = word
                # 어디까지 그 한글에 해당하는 한자인지 확인
                check_len = 0
                cnt = 1
                while True:
                    if ran_num2+cnt < len(line): # line 리스트의 인덱스를 벗어나지 않는 범위안에서만 체크
                        check_text = line[ran_num2+cnt]

                    if korean_check.match(check_text): # 그 다음으로 나오는 한글을 만났다면
                        check_len = cnt - 1
                        break
                    elif check_text == '\n':
                        check_len = cnt - 1
                        break

                    cnt += 1

                # 범위 안에서 다시 랜덤 수를 추출, ran_num2에 더해서 그 한글에 맞는 한자 랜덤 지정
                chn_text = line[ran_num2 + random.randint(1,check_len)]

            # 한자가 선택되었다면 -> 앞으로 거슬러 올라가 가장 먼저 발견하는 한글을 선택
            elif china_check.match(word):
                chn_text = word
                cnt = 1
                while True:
                    kor_text = line[ran_num2-cnt] 
                    if korean_check.match(kor_text):
                        break
                    cnt += 1
            # 그 외 다른 것이 선택되었다면
            else :
                pass
        if chn_text != origin_text :
            kor_lable.config(text=kor_text)
            chn_lable.config(text=chn_text)
            explain_lable.config(text = "검색을 누르면 글자 뜻을 검색해옵니다.")
            break

### layout 구현

## 상단 프레임 -> 정보 등
top_frame = Frame(root)
top_frame.pack(fill='x', expand=True)

top_label = Label(top_frame, text='Search From : Daum / Jay code')
top_label.pack(side='right',padx=5)


## 글자 프레임
lettter_frame = Frame(root)
lettter_frame.pack(pady=10)

# 1) 왼쪽 프레임 -> 한글 넣기
left_frame = Frame(lettter_frame, relief='solid', borderwidth=5)
left_frame.pack(side='left')

um_label = Label(left_frame, text = '음(音)', padx=50)
um_label.pack(side ='top')

kor_lable = Label(left_frame, text=kor_text ,font=(NONE,100), padx=50,pady=100)
kor_lable.pack()

# 2) 오른쪽 프레임 -> 한자 넣기
right_frame = Frame(lettter_frame, relief='solid', borderwidth=5)
right_frame.pack(side='right')

ja_label = Label(right_frame, text = '자(字)', padx=50)
ja_label.pack(side ='top')

chn_lable = Label(right_frame, text=chn_text, font=(NONE,100),padx=50,pady=100)
chn_lable.pack()


## 하단 프레임
bottom_frame = Frame(root)
bottom_frame.pack(side = 'bottom')

# 해설 레이블
explain_lable = Label(bottom_frame, text = "검색을 누르면 글자 뜻을 검색해옵니다.")
explain_lable.pack(side = 'top')

# 넘어가기용 버튼
btn_next = Button(bottom_frame, text = '다음', width=10, height=2, command=go_next)
btn_next.pack(side='left', pady = 10, padx = 5)

# 검색용 버튼
btn_naver = Button(bottom_frame, text = '검색', width=10, height=2, command=go_search)
btn_naver.pack(side='right', pady=10, padx = 5)

root.mainloop()