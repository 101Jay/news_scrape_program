import csv
import requests
from bs4 import BeautifulSoup

for i in range(0,2):
    url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok={0}&page=".format(i)
    if i == 0:
        name = "코스피"
    else:
        name = "코스닥"
    file = open("{0} 시가총액 순위 1-200.csv".format(name), "w", encoding="utf-8-sig",newline="") # 엑셀 파일이 깨진다 싶으면 utf-8-sig로 해주면 됨
    writer = csv.writer(file)
    name_data = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE".split('\t') # 이렇게 하면 리스트 형태로 저장됨
    writer.writerow(name_data)

    for page in range(1,5):
        res = requests.get(url+str(page))
        res.raise_for_status()
        soup = BeautifulSoup(res.text,"lxml")

        data_rows = soup.find("table", attrs={"class" : "type_2"}).find("tbody").find_all("tr")
        for row in data_rows:
            colunms = row.find_all("td")
            if len(colunms) <= 1 :
                continue # 이상한 데이터 제거
            data_col = [data.get_text().strip() for data in colunms]
            writer.writerow(data_col) # 리스트 형태를 인자로 받음