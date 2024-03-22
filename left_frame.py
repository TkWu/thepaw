# left_frame.py
import tkinter as tk
from tkinter import ttk

room_types = ["Luxury Suite", "Ocean View", "Standard", "Family", "Superior"]
price_labels = ["Weekday Price", "Weekend Price", "Holiday Price"]

def create_left_frame(parent):
    left_frame = tk.Frame(parent, width=200, height=400, bg='lightblue')
    left_frame.pack_propagate(False)
    
     # 创建三个表格
    for i, label_text in enumerate(price_labels):
        frame = ttk.Frame(left_frame)
        frame.grid(row=i, column=0, padx=10, pady=5, sticky="nsew")

        # 创建 Label 显示价格标签文本
        label = tk.Label(frame, text=label_text)
        label.pack()

        # 创建表格
        table = ttk.Treeview(frame)
        table["columns"] = ("1", "2", "3")

        # 设置列的标题
        table.heading("#0", text="ID")
        table.heading("1", text="Name")
        table.heading("2", text="Age")
        table.heading("3", text="City")

        # 添加示例数据
        table.insert("", "end", text="1", values=("John Doe", "30", "New York"))
        table.insert("", "end", text="2", values=("Jane Smith", "25", "Los Angeles"))
        table.insert("", "end", text="3", values=("Mike Johnson", "40", "Chicago"))

        # 显示表格
        table.pack()
    
    # Room types and prices input section
    
    entry_prices = {}
    
    for i, price_label in enumerate(price_labels):
        entry_prices[price_label] = {}
        tk.Label(left_frame, text=price_label).grid(row=i, column=0, padx=10, pady=5, sticky="w")

        for j, room_type in enumerate(room_types):
            entry_prices[price_label][room_type] = tk.StringVar()
            entry = tk.Entry(left_frame, textvariable=entry_prices[price_label][room_type], width=10)
            entry.grid(row=i, column=j+1, padx=10, pady=5)

    # Button to save room types and prices
    save_button = tk.Button(left_frame, text="Save", command=save_configuration)
    save_button.grid(row=len(price_labels)+1, column=0, columnspan=len(room_types)+1, padx=10, pady=10)

    # Button to load room types and prices
    load_button = tk.Button(left_frame, text="Load", command=load_configuration)
    load_button.grid(row=len(price_labels)+2, column=0, columnspan=len(room_types)+1, padx=10, pady=10)

    

    
    return left_frame

def save_configuration():
    # Function to save room types and prices to a configuration file
    # You can implement the logic here
    pass

def load_configuration():
    # Function to load room types and prices from a configuration file
    # You can implement the logic here
    pass