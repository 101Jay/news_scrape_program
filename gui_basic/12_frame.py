#gui : grapical user interface
from tkinter import *

root = Tk()
root.title("Jay_code")
root.geometry("500x500+3000+100") # 오른쪽 모니터에서 출력되도록

Label(root, text = "메뉴를 선택해주세요").pack(side = "top")

Button(root, text = "주문하기").pack(side = "bottom")

# 메뉴 프레임
frame_burger = Frame(root, relief="solid", bd = 1)
frame_burger.pack(side = "left", fill = "both", expand = True)

for i in ["햄버거", "치즈버거", "치킨버거"] :
    Button(frame_burger, text = i,).pack() # 프레임 안에 버튼 집어넣기

frame_drink = LabelFrame(root, text="음료")
frame_drink.pack(side="right", fill="both", expand = True)

for i in ["코카콜라", "스프라이트", "마운틴듀"] :
    Button(frame_drink, text = i,).pack() # 프레임 안에 버튼 집어넣기

root.mainloop()