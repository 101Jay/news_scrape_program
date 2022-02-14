# dir() : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시

# print(dir())
# import random
# print(dir())

# lst = [1,2,3]
# print(dir(lst)) #-> 리스트가 어떤 함수를 갖는지 표시

#구글 -> list of python builtins 검색 여러 내장 함수 확인 가능.

#외장 함수 -> list of python modules

# glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir)
# import glob
# print(glob.glob("*.py"))

# os : 운영체제에서 제공하는 기본 기능
# import os
# print(os.getcwd()) #현재 작업중인 디렉토리 확인

# folder = "sample_dir"

# if os.path.exists(folder):
#     print("이미 존재하는 폴더입니다.")
#     os.rmdir(folder)
# else :
#     os.makedirs(folder) #폴더 생성
#     print(folder, "폴더를 생성하였습니다.")
# print(os.listdir())


# import time
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S"))

# import datetime
# print("오늘 날짜는 ", datetime.date.today())

#timedelta : 두 날짜 사이의 간격
# today = datetime.date.today() #오늘 날짜
# td = datetime.timedelta(days=100)
# print("우리가 만난지 100일은", today + td)