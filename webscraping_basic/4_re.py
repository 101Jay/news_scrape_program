import re

p = re.compile("ca.e") # 정규식

'''
. (ca.e) : 하나의 문자를 의미 -> cafe, care 
^ (^de) : 문자열의 시작 -> desk, destination
$ (se$) : 문자열의 끝 -> case, base, cease

'''

def print_excute(m):
    if m : # 매치 되었으면
        print("m.group() :", m.group()) # 일치하는 문자열 반환
        print("m.string :", m.string) # 입력받은 문자열
        print("m.start() :", m.start()) # 일차하는 문자열의 시작 index 
        print("m.end() :", m.end()) # 일차하는 문자열의 끝 index 
        print("m.span() :", m.span()) # 일차하는 문자열의 시작 / 끝 index 
    else :
        print("매칭되지 않음")

# m = p.match("careless") # 매치 되는지 확인할 대상 입력
# print_excute(m)
# match : 주어진 문자열의 '처음'부터 일치하는지 확인 -> 따라서, careless도 가능

# m = p.search("good care") # search : 주어진 문자열 중에 일치하는게 있는지 확인(처음이 아니어도 됨)
# print_excute(m)

lst = p.findall("good care cafe") # 일치하는 모든 것을 '리스트' 형태로 반환
print(lst)

# 1. p = re.compile("원하는 정규식")
# 2. m = p.match / search / findall ("비교할 문자열")
# 3. m.group() / string / start() / end / span
# more about... w3schools.com  / python re