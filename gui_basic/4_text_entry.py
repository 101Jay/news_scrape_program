#gui : grapical user interface
from tkinter import *

root = Tk()
root.title("Jay_code")
root.geometry("500x500+3000+100") # 오른쪽 모니터에서 출력되도록

txt = Text(root, width = 30, height = 5)
txt.pack()
txt.insert(END, "글자를 입력하세요") # 기본으로 입력되어있는 텍스트 설정

e = Entry(root, width = 30) # 엔트리는 한 줄로만 입력할 수 있는 형태
e.pack()
e.insert(0, "한 줄만 입력해요")

def btncmd() :
    # 내용 출력
    print(txt.get("1.0", END)) # 1 : 첫 번째 라인, 0 : 0 번째 colunm 위치를 의미
    print(e.get())

    # 위젯에 있는 내용 삭제
    txt.delete("1.0", END)
    e.delete(0, END)

btn = Button(root, text = "Click", command = btncmd)
btn.pack()

root.mainloop()