#gui : grapical user interface
import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("Jay_code")
root.geometry("500x500+3000+100") # 오른쪽 모니터에서 출력되도록

combo_values = [str(i) + "일" for i in range(1,32)]
combobox = ttk.Combobox(root, height = 5, values = combo_values, state = "readonly") 
# state설정을 통해 사용자가 임의의 값을 입력하는 것을 방지함
combobox.set("카드 결제일 선택") # 시작 값 세팅
combobox.pack()


def btncmd():
    print(combobox.get()) # values가 아닌 combobox를 직접 이용하여 값을 가져옴

btn = Button(root, text = "click", command= btncmd)
btn.pack()

root.mainloop()