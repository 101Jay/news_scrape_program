#gui : grapical user interface
from tkinter import *

root = Tk()
root.title("Jay_code")
root.geometry("500x500+3000+100") # 오른쪽 모니터에서 출력되도록

btn_f16 = Button(root, text="F16", width=5, height=2)
btn_f17 = Button(root, text="F17", width=5, height=2)
btn_f18 = Button(root, text="F18", width=5, height=2)
btn_f19 = Button(root, text="F19", width=5, height=2)

btn_clear = Button(root, text="clear", width=5, height=2)
btn_equal = Button(root, text="=", width=5, height=2)
btn_div = Button(root, text="/", width=5, height=2) 
btn_point = Button(root, text="*", width=5, height=2)

btn_7 = Button(root, text="7", width=5, height=2)
btn_8 = Button(root, text="8", width=5, height=2)
btn_9 = Button(root, text="9", width=5, height=2)
btn_sub = Button(root, text="-", width=5, height=2)

btn_4 = Button(root, text="4", width=5, height=2)
btn_5 = Button(root, text="5", width=5, height=2)
btn_6 = Button(root, text="6", width=5, height=2)
btn_add = Button(root, text="+", width=5, height=2)

line_four_add = [btn_f16, btn_f17, btn_f18, btn_f19, btn_clear, btn_equal, btn_div, btn_point, \
    btn_7, btn_8, btn_9, btn_sub, btn_4, btn_5, btn_6, btn_add] 

cnt = 0
row_span = 0

for row in range(0,4):
    for col in range(0,4):
        line_four_add[col+cnt].grid(row = row, column = col, sticky = N+E+W+S, padx=3, pady=3) # 북동서남 방향으로 버튼을 꽉 채워줌
    cnt += 4

btn_1 = Button(root, text="1", width=5, height=2)
btn_2 = Button(root, text="2", width=5, height=2)
btn_3 = Button(root, text="3", width=5, height=2)
btn_enter = Button(root, text="enter", width=5, height=2)

btn_1.grid(row=4, column=0, sticky = N+E+W+S, padx=3, pady=3)
btn_2.grid(row=4, column=1, sticky = N+E+W+S, padx=3, pady=3)
btn_3.grid(row=4, column=2, sticky = N+E+W+S, padx=3, pady=3)
btn_enter.grid(row=4, column=3, rowspan=2, sticky = N+E+W+S) # rowspan : 현재 위치로부터 아래로 그 수만큼 합침

btn_0 = Button(root, text="0", width=5, height=2)
btn_dot = Button(root, text=".", width=5, height=2)

btn_0.grid(row=5, column=0, columnspan=2, sticky = N+E+W+S, padx=3, pady=3) # colunmspan : 현재 위치로부터 오른쪽으로 그 수만큼 합침
btn_dot.grid(row=5, column=2, sticky = N+E+W+S, padx=3, pady=3)


root.mainloop()