#gui : grapical user interface
from tkinter import *

root = Tk()
root.title("Jay_code")
root.geometry("500x500+3000+100") # 오른쪽 모니터에서 출력되도록

def create_new_file():
    print("새 파일을 만듭니다.")

menu = Menu(root)

# File 메뉴 추가
menu_file = Menu(menu, tearoff = 0)
menu_file.add_command(label = "New File", command = create_new_file)
menu_file.add_command(label = "New Window")
menu_file.add_separator()
menu_file.add_command(label = "Open File")
menu_file.add_separator()
menu_file.add_command(label = "Save All", state = "disable") # 비활성화
menu_file.add_separator()
menu_file.add_command(label = "Exit", command=root.quit)
menu.add_cascade(label = "File", menu = menu_file)

# Edit 메뉴 추가
menu.add_cascade(label="Edit") # 빈 값만 메뉴에 추가

# Select 메뉴 추가
menu_selection = Menu(menu, tearoff= 0)
menu_selection.add_radiobutton(label = "Python")
menu_selection.add_radiobutton(label = "Java")
menu_selection.add_radiobutton(label = "C++")
menu.add_cascade(label = "Selection", menu = menu_selection)

# View 메뉴 추가 
menu_view = Menu(menu, tearoff=0)
menu_view.add_checkbutton(label="Show Minimap")
menu.add_cascade(label="View", menu=menu_view)

root.config(menu = menu)
root.mainloop()