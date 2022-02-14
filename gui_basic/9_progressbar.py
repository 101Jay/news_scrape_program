#gui : grapical user interface
import time
import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("Jay_code")
root.geometry("500x500+3000+100") # 오른쪽 모니터에서 출력되도록

progressbar1 = ttk.Progressbar(root, maximum = 100, mode = "indeterminate") # indeterminate -> 계속 왔다 갔다 함
progressbar1.start(500) # 500ms, 즉 0.5초마다 움직임
progressbar1.pack()

p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum = 100, length = 150, variable = p_var2)
progressbar2.pack()

def btncmd():
    for i in range(1,101):
        time.sleep(0.01) # 0.01초 대기

        p_var2.set(i) # p_var 값 설정
        progressbar2.update() # 값이 변하는 걸 보여주기 위해 지속적으로 업데이트(UI 업데이트)
        print(p_var2.get()) # 값을 얻어옴
 
btn = Button(root, text = "click", command= btncmd)
btn.pack()

root.mainloop()