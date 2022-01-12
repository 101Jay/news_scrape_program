kor = ["사과", "바나나", "오렌지"]
eng = ['apple', 'banana', 'orange']

print(list(zip(kor,eng))) # kor[0],eng[0] ... 형태로 합쳐주는 함수 zip

# unzip
mixed = [('사과', 'apple'), ('바나나', 'banana'), ('오렌지', 'orange')]
print(list(zip(*mixed))) # zip(*) 형태로 zip을 사용하면 각각의 인덱스 별로 나눠줌

kor2, eng2 = zip(*mixed) # 이와 같은 형태로 사용해주면 변수선언할 때 유용하다
print(kor2)
print(eng2)