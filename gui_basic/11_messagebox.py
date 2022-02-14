#gui : grapical user interface
import tkinter.messagebox as msgbox
from tkinter import *


root = Tk()
root.title("Jay_code")
root.geometry("500x500+3000+100") # 오른쪽 모니터에서 출력되도록

def btncmd():
    msgbox.showinfo("알림", "예매가 완료되었습니다.")

def btncmd1():
    msgbox.showwarning("경고", "매진된 좌석입니다.")

def btncmd2():
    msgbox.showerror("에러", "결제가 취소되었습니다.") # 알림 이모티콘과 소리가 달라짐

def btncmd3():
    msgbox.askokcancel("확인 / 취소", "결제를 진행하시겠습니까?")

def btncmd4():
    msgbox.askretrycancel("재시도 / 취소", "일시적인 오류입니다. 다시 시도하시겠습니까?")

def btncmd5():
    response = msgbox.askyesnocancel(None, "일시적인 오류입니다. 다시 시도하시겠습니까?") # 값을 받고 싶으면 변수 선언해서 받아오면 됨. 
    print("응답 : ", response) # True, False, None -> 예 : 1, 아니오 : 0 , 그 외 
    if response == 1 :
        print("예")
    elif response == 0 :
        print("아니오")
    else : 
        print("취소")

Button(root, text="알림", command = btncmd5).pack()



root.mainloop()