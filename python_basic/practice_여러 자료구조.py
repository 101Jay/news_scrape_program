#리스트
#append, insert, pop, sort, count, reverse, clear
#다양한 자료형 합께 사용 가능
#extend -> 리스트 자체로 확장 가능

# my_list = ['아이유', '에스파', '트와이스']

# my_list.insert(2,'마마무')

# my_list.clear()

# print(my_list)

#사전
#print(3 in cabinet)
#get 함수의 차이점
#할당 => cabinet[5] = '조세호'
#덮어씌우기 가능
#del cabinet[3] 
#cabinet.keys / values / items / clear

# cabinet = {3:"유재석"}
# print(cabinet[3])
# print(cabinet.get(1, '사용 가능'))  #get은 오류 안내고 none을 리턴해줌.

# print(32 in cabinet)
# cabinet[5] = '아이유'
# cabinet[3] = '에스파'
# print(cabinet.items())
# print(cabinet.keys())
# print(cabinet.values())
# print(cabinet.clear())

#튜플 -> 내용 변경 및 추가 불가!!!!
#한 번에 변수 선언시에 편리하다!

# age = 30
# name = "ki"
# hobby = "coding"

# (age, name, hobby) = 30, "ki", "coding"

# 집합 : 중복 안 됨, 순서 없음
# 교집합 : & / .intersection / 
# 합집합 : | / .union
# 차집합 : .difference / '-'
# .add() / .remove(  )

# my_set = {'유재석', '아이유', '에스파', '트와이스'}
# new_set = set(['유재석','박명수', '김종국'])
# print(my_set)
# print(new_set)

# print(my_set.intersection(new_set))
# print(my_set.union(new_set))
# print(my_set.difference(new_set))

# my_set.add('김종국')
# print(my_set)

# my_set.remove('트와이스')
# print(my_set)

#자료구조의 변경
# my_set = {'유재석', '아이유', '에스파', '트와이스'}
# print(my_set, type(my_set))
# my_set = list(my_set)
# print(my_set, type(my_set))
# my_set = tuple(my_set)
# print(my_set, type(my_set))
