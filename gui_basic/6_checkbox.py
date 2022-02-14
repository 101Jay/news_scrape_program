#gui : grapical user interface
from tkinter import *

root = Tk()
root.title("Jay_code")
root.geometry("500x500+3000+100") # 오른쪽 모니터에서 출력되도록

chkvar = IntVar()
chkbox = Checkbutton(root, text = "오늘 하루 보지 않기", variable= chkvar) # variable을 설정해줘야 한다.
# chkbox.select() # 기본 선택 처리 -> 디폴트는 선택 해제 상태
chkbox.pack()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text = "일주일동안 보지 않기", variable = chkvar2)
chkbox2.pack()


def btncmd():
    print(chkvar.get()) # 0 : 체크 해제, 1 : 체크
    print(chkvar2.get())

btn = Button(root, text = "click", command= btncmd)
btn.pack()

root.mainloop()