#gui : grapical user interface
from tkinter import *

root = Tk()
root.title("Jay_code")

btn1 = Button(root, text='버튼1')
btn1.pack()

btn2 = Button(root, padx=5, pady=10, text="버튼2")  # 글자 크기에 따라 버튼 크기 가변
btn2.pack()

btn3 = Button(root, width = 10, height = 10, text="버튼3") # 글자 크기와 상관 없이 고정된 너비, 높이
btn3.pack()

btn4 = Button(root, fg='red', bg = 'black', text = '버튼5') # 배경, 글자 색 입력
btn4.pack()

photo = PhotoImage(file="gui_basic/img.png")
btn6 = Button(root, image = photo)
btn6.pack()

def btncmd():
    print("버튼이 클릭되었어요!")

btn7 = Button(root, text='동작하는 버튼', command = btncmd) # 버튼 눌렀을 때 동작하도록 설정
btn7.pack()

root.mainloop()