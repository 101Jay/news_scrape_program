import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("image_merge")
root.geometry("500x555+3000+100") # 가로 * 세로 + x좌표 + y좌표

# 파일 프레임 (파일 추가, 선택 삭제)
file_frame = Frame(root)
file_frame.pack(fill = 'x', padx=5, pady=5)

btn_add_file = Button(file_frame, text = "파일추가", width = 8,height = 2)
btn_add_file.pack(side="left", padx=15,pady=3)
btn_del_file = Button(file_frame, text = "선택삭제", width = 8,height = 2)
btn_del_file.pack(side="right", padx=15,pady=3)



# 리스트 프레임
list_frame = Frame(root)
list_frame.pack(fill='both', expand=True, padx=5, pady=5)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill='y')

list_file = Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=scrollbar.set)
list_file.pack(side='left', fill='both', expand=True)
scrollbar.config(command=list_file.yview)



# 저장 경로 프레임
path_frame = LabelFrame(root, text = "저장경로") # 프레임 이름을 넣고 싶다면 LabelFrame 사용
path_frame.pack(fill = 'x', padx=5, pady=5, ipady=3)

txt_save_path = Entry(path_frame) # 한 줄만 입력
txt_save_path.pack(side='left', fill='x', expand=True, padx=5, pady=5) 

btn_find_path = Button(path_frame, text = "찾아보기", width=10)
btn_find_path.pack(side="right", padx=5, pady=5)



# 옵션 프레임
option_frame = LabelFrame(root, text="옵션")
option_frame.pack(fill = 'x', expand=True, padx=5, pady=5, ipady=3)

# 1. 가로 넓이 옵션
width_label = Label(option_frame, text="가로넓이", width=8)
width_label.pack(side='left', pady=3)

width_combo_value = ["원본유지", "1024", "800", "640"]
width_combobox = ttk.Combobox(option_frame, values = width_combo_value, width=10, state = "readonly")
width_combobox.current(0) # .set("원본유지")
width_combobox.pack(side='left', pady=3)

# 2. 간격 옵션
betw_label = Label(option_frame, text="간격", width=8)
betw_label.pack(side='left', pady=3)

betw_combo_value = ["없음", "좁게", "보통", "넓게"]
betw_combobox = ttk.Combobox(option_frame, values = betw_combo_value, width=10, state = "readonly")
betw_combobox.current(0)
betw_combobox.pack(side='left', pady=3) # left로 해줘야 가로로 죽 나열됨

# 3. 포맷 옵션
format_label = Label(option_frame, text="포맷", width=8)
format_label.pack(side='left', pady=3)

format_combo_value = ["PNG", "JPG", "BMP"]
format_combobox = ttk.Combobox(option_frame, values = format_combo_value, width=10, state = "readonly")
format_combobox.current(0)
format_combobox.pack(side='left', pady=3)



# 프로그레스 프레임
pro_frame = LabelFrame(root, text="진행상황")
pro_frame.pack(fill='x', padx=5, pady=5, ipady=3)

pro_value = DoubleVar()
progressbar = ttk.Progressbar(pro_frame, maximum=100, variable=pro_value)
progressbar.pack(fill='x', padx=3,pady=3)

# pro_value 설정 필요



# 실행 프레임
process_frame = Frame(root)
process_frame.pack(fill='both', padx=5, pady=5, ipady=3)


btn_exit = Button(process_frame, text = "닫기", padx=5, pady=5, width=12, height=20, command=root.quit)
btn_exit.pack(side='right', padx=5, pady=5)
btn_start = Button(process_frame, text="시작", padx=5, pady=5, width=12, height=20)
btn_start.pack(side='right', padx=5, pady=5)



root.resizable(False, False)  # 창 가로 / 세로로 늘이기 허용 안 함
root.mainloop()