class BigNumberError(Exception): #사용자 정의 에러
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return self.msg

try:
    print("한 자리수 나누기 전용 계산기")
    num1 = int(input("press first number : "))
    num2 = int(input("press second number : "))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError("입력값 : {0}, {1}".format(num1, num2)) #에러 발생시키기
    print("{0} / {1} = {2}".format(num1,num2,num1/num2))

except ValueError as err:
    print("잘못된 값이 입력되었습니다. 한 자리 숫자만 입력하세요.")
    print(err)

except ZeroDivisionError :
    print("You can't devide by zero")

except BigNumberError as err: #사용자 정의 에러
    print("두 자리 수 이상의 값입니다. 한 자리 숫자만 입력해주세요.")
    print(err)

except Exception as err:
    print("알 수 없는 에러가 발생했습니다.\n에러 정보:")
    print(err)

finally : 
    print("계산기를 이용해 주셔서 감사합니다.")
