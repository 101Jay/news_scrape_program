import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
import os
from tkinter import * # __all__에 지정되어 있지 않은 것들은 *로도 임포트 불가
from tkinter import filedialog


root = Tk()
root.title("image_merge")
root.geometry("500x545+3000+100") # 가로 * 세로 + x좌표 + y좌표

# 함수 정의
file_path = os.path.dirname("/pygame_project/images")

# 파일추가
def add_file():
    files = filedialog.askopenfilenames(title="이미지 파일을 선택하세요", filetypes=(("PNG 파일", "*.png"), ("모든 파일","*.*")), \
        initialdir = file_path)
    for file in files:
        list_file.insert(END,file)

# 선택삭제
def del_file():
    sel_file = list_file.curselection()
    for i in reversed(sel_file): # 뒤에서부터 가져와야 할 때! list.reverse()와 달리 실제로 그 리스트가 바뀌는 건 아님
        list_file.delete(i)

# 저장경로
def find_path():
    folder_selected = filedialog.askdirectory()
    if folder_selected == '': # 사용자가 취소를 누를 때
        return 
    txt_save_path.delete(0,END) # 값이 있었을 수도 있으니 일단 삭제 먼저 해줘야함
    txt_save_path.insert(0, folder_selected)

# 시작
def start():
    # 이미지 파일 있는지 확인
    if list_file.size() == 0 :
        msgbox.showerror("에러", "이미지 파일이 없습니다")
    elif len(txt_save_path.get()) == 0 :
        msgbox.showerror("에러", "저장경로를 설정하세요")


# 파일 프레임 (파일 추가, 선택 삭제)
file_frame = Frame(root)
file_frame.pack(fill = 'x', padx=5, pady=5)

btn_add_file = Button(file_frame, text = "파일추가", width = 10, command=add_file)
btn_add_file.pack(side="left", padx=15,pady=3)
btn_del_file = Button(file_frame, text = "선택삭제", width = 10, command=del_file)
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

btn_find_path = Button(path_frame, text = "찾아보기", width=10, command=find_path)
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
btn_start = Button(process_frame, text="시작", padx=5, pady=5, width=12, height=20, command = start)
btn_start.pack(side='right', padx=5, pady=5)



root.resizable(False, False)  # 창 가로 / 세로로 늘이기 허용 안 함
root.mainloop()