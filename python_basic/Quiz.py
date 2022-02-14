'''1. 사이트별로 비밀번호를 만들어주는 프로그램을 작성하시오.

url = input("Press the site name\n")
my_str = url[7:url.find(".")]

password = my_str[:3] + str(len(my_str)) + str(my_str.count('e')) + '!'

print("생성된 비밀번호 : %s" % password)'''

'''2. 코딩 대회 당첨자 추첨 프로그램 작성

from random import *

#writer 리스트 만들기
# writer = []
# for i in range(21):
#     writer.append(i)
# writer.remove(0)
# print(writer)

writer = range(1,21)
writer = list(writer)

#추첨하기
shuffle(writer)
first_prize = sample(writer,1)
writer.remove(first_prize[0])
shuffle(writer)
second_prize = sample(writer,3) 
print("--당첨자 발표--\n치킨 당첨자 : %s\n커피 당첨자 : %s\n--축하합니다--" % (first_prize[0], second_prize))
'''

'''
#3. 카카오 택시 기사님 승객 수 구하기 프로그램

from random import *

customer = []

for index in range(50):
    customer.append(randrange(5,51))

cnt = 0

for i in range(50):
    if customer[i] <= 15 :
        print('[O] {0}번째 손님 (소요시간 : {1}분)'.format(i+1,customer[i]))
        cnt += 1
    else :
        print('[ ] {0}번째 손님 (소요시간 : {1}분)'.format(i+1,customer[i]))

print('총 탑승 승객 : {0} 분'.format(cnt))
'''

'''
#4. 표준 체중을 구하는 프로그램을 작성하시오.

def std_weight(height, gender): #키는 M, 성별은 '남자', '여성'으로 받음
    if gender == '남자':
        standard = round(height**2 * 22, 2)
    else : 
        standard = round(height**2 * 21, 2)
    return standard

gender = input('당신의 성별은?')
height = input('당신의 키는?')

print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender,std_weight((float(height) / 100), gender)))
'''

'''
#5. 매주 1회 작성해야하는 보고서

for index in range(1,51):
    with open("{0}주차.txt".format(index), "w", encoding="utf8") as report:
        report.write("- {0}주차 업무보고 - \n부서:   \n이름:   \n업무 요약: \n".format(index))
'''

'''
#6. 부동산 프로그램 작성
출력 예제:

총 3대의 매물이 있습니다.
강남 아파트 매매 10억 2010년
마포 오피스텔 전세 5억 2007년
송파 빌라 월세 500/50 2000년

#참고 코드
class House:
    #매물 초기화
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year
    #매물 정보 표시 
    def show_detail(self):
        print("{0} {1} {2} {3} {4}".format(self.location, self.house_type, self.deal_type, self.price, self.completion_year))

gangnam = House("강남", "아파트", "매매", "10억", "2010년")
mapo = House("마포", "오피스텔", "전세", "5억", "2007년")
songpa = House("송파", "빌라", "월세", "500/50", "2000년")

houses = [gangnam, mapo, songpa]

print("총 {0}대의 매물이 있습니다.".format(len(houses)))
for house in houses:
    house.show_detail()
'''

'''
#7.치킨 자동 주문 시스템

class SoldOutError(Exception):
    def __init__(self):
        pass

chicken = 10
waiting = 1 #홀 만석, 대기 번호 1번부터 시작
while True :
    print("남은 치킨 : {0}마리".format(chicken))
    try:
        order = int(input("치킨을 몇 마리 주문하시겠습니까? :"))
        if order < 1 :
            raise ValueError
        if order > chicken : #남은 치킨보다 주문량이 많을 때
            print("재료가 부족합니다.")
        else : 
            print("[대기번호 {0}번] 치킨 {1}마리 주문이 완료되었습니다.".format(waiting, order))
            waiting += 1
            chicken -= order
            if chicken == 0 :
                raise SoldOutError

    except ValueError:
        print("잘못된 값을 입력하였습니다.")
    except SoldOutError:
        print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
        break

'''
'''
#10. byme 모듈 만들기
import byme
byme.sign("조코딩", "http://jocoding_youtube.com", "Jocoding@gamail.com")
'''