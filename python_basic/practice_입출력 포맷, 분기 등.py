#input, if/elif/else, or/and 사용 가능

# weather = input("오늘 날씨 어때요? ")
# if weather == '비' or weather == '눈':
#     print("우산을 챙기세요")
# elif weather == '미세먼지':
#     print("마스크를 챙기세요")
# else :
#     print("준비물이 필요 없는 날씨네요")

#for

#while

# customer = '토르'
# index = 5
# while index >= 1 :
#     print("{0}님, 커피 나왔습니다. {1}번만 더 불러드릴게요.".format(customer, index))
#     index -= 1
#     if(index == 0):
#         print('커피는 제가 마실게요 그냥')

#continue-> 아래에 있는거 건너뛰고 반복문 진행.
#break -> 바로 반목문 탈출

#한줄 for

# students = [1,2,3,4,5]

# students = [i+100 for i in students]

# students = ['Iron man', 'Thor', 'Grute']

# students = [len(i) for i in students]
# print(students)


#함수
# def withdraw_night(balance, money):
#     commission = 100 # 수수료 100원
#     return commission, balance - money - commission

# balance = 5000
# commission, balance = withdraw_night(balance, 500) #튜플을 이용한 변수 선언!!!

# print("수수료 {0}원이며, 잔액은 {1}원입니다.".format(commission,balance))

#기본값
# def profile(name, age=17, main_lang="Python"):
#     print("이름 : {0},\t 나이 : {1}\t주 사용 언어 : {2}"\
#         .format(name, age, main_lang))

# profile('k')

#가변인자
# def profile(name,age, *language):
#     print("이름 : {0}\t나이: {1}\t".format(name,age),end=" ")
#     for lang in language : 
#         print(lang, end=" ")

# profile('IU', 30, 'kotlin','swift')

#전역변수 / 매개변수로 받아서 리턴해서 다시 받는 것이 코드 관리에 더 유용함

#문자열-> .ljust(), .rjust(), .zfill() 사용가능
#print ->  sep, end로 구분문자, 끝 문자 변경 가능
# scores = {"수학" : 0, "국어":50, "코딩":100}

# for subject, score in scores.items():
#     print(subject.ljust(8), str(score).rjust(8), sep=":")

# for num in range(1,31):
#     print("대기번호 :" + str(num).zfill(3))

#input으로 받아올 땐, 항상 문자열로 온다는 것 확인!

#다양한 출력 포맷
# print("{0: >10}".format(500))
# print("{0: >+10}".format(500))  
# print("{0:_<+10}".format(500))
# #빈칸 언더바로 채우기, 오른쪽정렬, 30칸 띄우기, 양수일 땐 +붙이기, 콤마로 3자리마다 나눠주기
# print("{0:_>+30,}".format(500000000000))

# print("{0:.2f}".format(3.14256)) #2째자리까지만 표시해달라.
