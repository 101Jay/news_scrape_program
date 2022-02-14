#gui : grapical user interface
from tkinter import *

root = Tk()
root.title("Jay_code")
root.geometry("500x500+3000+100") # 오른쪽 모니터에서 출력되도록

Label(root, text = "메뉴를 선택하세요").pack()

burger_var = StringVar()
btn_burger1 = Radiobutton(root, text = "불고기버거", value = "불고기버거", variable = burger_var)
btn_burger1.select() # 기본값으로 선택
btn_burger2 = Radiobutton(root, text = "치즈버거", value = "치즈버거", variable = burger_var)
btn_burger3 = Radiobutton(root, text = "치킨버거", value = "치킨버거", variable = burger_var)

drink_var = StringVar()
btn_drink1 = Radiobutton(root, text = "콜라", value = "콜라",  variable = drink_var)
btn_drink1.select() # 기본값으로 선택
btn_drink2 = Radiobutton(root, text = "사이다", value = "사이다",  variable = drink_var)
btn_drink3 = Radiobutton(root, text = "마운틴듀", value = "마운틴듀",  variable = drink_var)

menu_list = [btn_burger1, btn_burger2, btn_burger3, btn_drink1, btn_drink2, btn_drink3]
for i in menu_list :
    i.pack()


def btncmd():
    print(burger_var.get())
    print(drink_var.get())

btn = Button(root, text = "click", command= btncmd)
btn.pack()

root.mainloop()