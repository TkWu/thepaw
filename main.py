import tkinter as tk
from tkinter import ttk
from left_frame import create_left_frame
from right_frame import create_right_frame


main_frame_title = "Title"
main_frame_title = "red"
main_frame_title = "red"

left_frame_global_color = "red"
left_frame_global_color = "red"
left_frame_global_color = "red"
left_frame_global_color = "red"

def main():
    # 创建主窗口
    window = tk.Tk()
    window.geometry("1024x768")

    # 创建上半部分的 Frame
    top_frame = tk.Frame(window, width=1024, height=50, bg="blue")
    top_frame.pack(side="top", fill="x")

    # 使用 Label 显示标题
    title_label = tk.Label(top_frame, text=main_frame_title, font=("Helvetica", 16), bg="gray", fg="white")
    title_label.pack(expand=True, fill="both")

    # 创建左边的 Frame
    global left_frame
    left_frame = create_left_frame(window)
    left_frame.pack(side="left", fill="both", expand=True)

    # 创建右边的 Frame
    right_frame = create_right_frame(window)
    right_frame.pack(side="right", fill="both", expand=True)

    '''
    # 创建更新左边框架内容的按钮
    update_button = tk.Button(window, text="Update Left Frame", command=update_left_frame)
    update_button.pack(pady=10)
    '''

    # 启动主窗口
    window.mainloop()

'''
def update_left_frame():
    # 在这里编写更新左边框架内容的逻辑
    # 可以重新创建左边框架或者更新其中的部件内容
    global left_frame_global_color
    left_frame_ori_color = left_frame.cget("bg")
    
    if(left_frame_global_color != left_frame_ori_color):
        left_frame.configure(bg=left_frame_global_color)
        left_frame_global_color = left_frame_ori_color    
'''

if __name__ == "__main__":
    main()



