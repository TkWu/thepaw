import tkinter as tk
from tkinter import ttk
from left_frame import create_left_frame
from right_frame import create_right_frame

def main():
    # 創建主視窗
    window = tk.Tk()
    window.geometry("1024x768")

    # 創建上半邊的 Frame
    top_frame = tk.Frame(window, width=1024, height=50, bg="blue")
    top_frame.pack(side="top", fill="x")

    # 使用 Label 顯示標題
    title_label = tk.Label(top_frame, text="標題標題標題", font=("Helvetica", 16), bg="gray", fg="white")
    title_label.pack(expand=True, fill="both")

    # 強制更新上半邊的畫面
    top_frame.update()  

    # 創建左半邊的 Frame
    left_frame = create_left_frame(window)
    left_frame.pack(side="left", fill="both", expand=True)

    # 創建右半邊的 Frame
    right_frame = create_right_frame(window)
    right_frame.pack(side="left", fill="both", expand=True)

    # 強制更新左右兩邊的畫面
    left_frame.update()
    right_frame.update()

    # 啟動主視窗
    window.mainloop()

if __name__ == "__main__":
    main()
