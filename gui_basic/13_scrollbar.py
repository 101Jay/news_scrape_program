#gui : grapical user interface
from tkinter import *

root = Tk()
root.title("Jay_code")
root.geometry("500x500+3000+100") # 오른쪽 모니터에서 출력되도록

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y") # y축에 사이즈 맞춤, 오른쪽에 놓기

# scrollbar.set을 해줌으로써 리스트 박스에 스크롤을 연동
listbox = Listbox(frame, selectmode = "extended", height = 10, yscrollcommand = scrollbar.set)

for i in range(1,32):
    listbox.insert(END, str(i) + "일")
listbox.pack(side = "left")

# config를 통해 스크롤바에 리스트 박스를 연동 
scrollbar.config(command=listbox.yview)

# 두 개 다 연동시켜줘야함.

root.mainloop()