# window 메모장 만들기
from tkinter import *

root = Tk()
root.title("제목 없음 - Windows 메모장")
root.geometry("500x500+3000+100") # 가로 * 세로 + x좌표 + y좌표
root.resizable(True, True)  # 창 가로 / 세로로 늘이기 허용

# 스크롤바 세로 / 가로
scroll_bar = Scrollbar(root)
scroll_bar.pack(side="right", fill="y")
scroll_bar2 = Scrollbar(root, orient=HORIZONTAL) # 가로로 활용하기 위해 orient를 HORIZONTAL로 설정
scroll_bar2.pack(side="bottom", fill='x')

menu = Menu(root)
menu_file = Menu(menu, tearoff=0)

filename = "mynote.txt"

class file_sys:
    def __init__(self):
        self.mynote_text = Text(root, wrap = "none", yscrollcommand=scroll_bar.set,xscrollcommand=scroll_bar2.set) 
        # wrap 속성을 none으로 해야 가로로 늘어남 
        self.mynote_text.pack(fill = 'both', expand=True)

    def open_file(self):
        with open(filename, "r", encoding="utf-8") as memo_txt:
            # 무언가 있는 상태에서 열기하면 text에 있는 내용 지운 후 그것만 보이도록 하기 위해 삭제해준다.
            self.mynote_text.delete("1.0", END) 
            self.mynote_text.insert(END, memo_txt.read())

    def save_file(self):
        mynote_txt = self.mynote_text.get("1.0", END)
        with open(filename, "w", encoding="utf-8") as save_txt:
            save_txt.write(mynote_txt)

file_put = file_sys() # 클래스 선언

menu_file.add_command(label = "열기(O)", command=file_put.open_file) # command 다음에 함수 이름만! ()까지 쓰면 여기서 바로 실행됨.
menu_file.add_command(label = "저장(S)", command=file_put.save_file)
menu_file.add_separator()
menu_file.add_command(label = "끝내기(x)", command = root.quit)
menu.add_cascade(menu = menu_file, label="파일(F)")

# menu_edit = Menu(menu, tearoff=0)
# menu.add_cascade(menu = menu_edit, label="편집(E)") 이렇게 할 필요가 없다.
menu.add_cascade(label="편집(E)")
menu.add_cascade(label="서식(O)")
menu.add_cascade(label="보기(V)")
menu.add_cascade(label="도움말(H)")

scroll_bar.config(command=file_put.mynote_text.yview)
scroll_bar2.config(command=file_put.mynote_text.xview)

root.config(menu = menu)
root.mainloop()