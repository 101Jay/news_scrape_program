#gui : grapical user interface
from tkinter import *


root = Tk()
root.title("Jay_code")
root.geometry("500x500+3000+100") # 오른쪽 모니터에서 출력되도록

listbox = Listbox(root, selectmode='single', height = 0) # height를 지정해주면 그 숫자만큼의 목록만 화면에 표시
listbox.insert(0, "질럿")
listbox.insert(1, "저글링")
listbox.insert(END, "히드라") # END를 이용해 가장 마지막에 넣어줄 수 있다
listbox.insert(END, "하이템플러")
listbox.pack()

def btncmd() :
    # 삭제
    # listbox.delete(END) # 가장 뒤 항목 삭제

    # 갯수 출력
    print("리스트 박스에는", listbox.size(), "개가 있습니다.")

    # 항목 확인
    print(listbox.get(0,END)) # 인덱스로 어느 항목 확인할 건지 지정

    # 선택 항목 확인
    print(listbox.get(listbox.curselection())) # curselection은 선택된 항목의 인덱스 값 반환

btn = Button(root, text = "Click", command = btncmd)
btn.pack()

e = Entry(root, width = 30)
e.pack()
e.insert(0, "유닛을 추가하세요") # 어느 위치에 추가할지도 지정해주긴 해야함

def list_append():
    global get_text
    get_text = e.get()
    listbox.insert(END, get_text)

btn2 = Button(root, text = "append", command= list_append)
btn2.pack()

root.mainloop()