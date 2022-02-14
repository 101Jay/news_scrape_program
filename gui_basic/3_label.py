#gui : grapical user interface
from tkinter import *

root = Tk()
root.title("Jay_code")
root.geometry("500x500+3000+100") # 오른쪽 모니터에서 출력되도록

label1 = Label(root, text = "안녕하세요!") # 글자나 이미지를 보여줄 뿐, 뭔가 동작하진 않음
label1.pack()

photo = PhotoImage(file = "gui_basic/img.png")
label2 = Label(root, image = photo)
label2.pack()

def change():
    label1.config(text="See U soon")

    global photo2 # Garbage Collection -> 전역 변수로 만들지 않으면 필요 없는 건줄 알고 메모리 공간 해제
    photo2 = PhotoImage(file = "gui_basic/img2.png")
    label2.config(image = photo2)

btn = Button(root, text = "Click to change", command = change)
btn.pack()

root.mainloop()