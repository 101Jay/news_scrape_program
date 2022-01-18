from cgitb import text
from attr import attr
import requests
from bs4 import BeautifulSoup

url = 'https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english#;'
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

text_box = soup.find_all("div", attrs={"class" : "conv_txt"})
eng_text = text_box[1].find_all("span", attrs = {"class" : "conv_sub"})
kor_text = text_box[0].find_all("span", attrs = {"class" : "conv_sub"})

print("[오늘의 영어 회화]")
print("(영어 지문)")
for i in eng_text:
    print(i.get_text())
print("\n")
print("(한글 지문)")
for i in kor_text:
    print(i.get_text())