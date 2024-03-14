# right_frame.py
import tkinter as tk

def create_right_frame(parent):
    right_frame = tk.Frame(parent, width=200, height=400, bg='lightgreen')
    right_frame.pack_propagate(False)

    # Pet details input fields
    pet_name_label = tk.Label(right_frame, text="Pet Name:")
    pet_name_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
    pet_name_entry = tk.Entry(right_frame)
    pet_name_entry.grid(row=0, column=1, padx=10, pady=5)

    pet_weight_label = tk.Label(right_frame, text="Pet Weight:")
    pet_weight_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
    pet_weight_entry = tk.Entry(right_frame)
    pet_weight_entry.grid(row=1, column=1, padx=10, pady=5)

    pet_type_label = tk.Label(right_frame, text="Pet Type:")
    pet_type_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
    pet_type_var = tk.StringVar()
    pet_type_dog = tk.Radiobutton(right_frame, text="Dog", variable=pet_type_var, value="Dog")
    pet_type_dog.grid(row=2, column=1, padx=10, pady=5)
    pet_type_cat = tk.Radiobutton(right_frame, text="Cat", variable=pet_type_var, value="Cat")
    pet_type_cat.grid(row=2, column=2, padx=10, pady=5)

    start_date_label = tk.Label(right_frame, text="Start Date:")
    start_date_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
    start_date_entry = tk.Entry(right_frame)
    start_date_entry.grid(row=3, column=1, padx=10, pady=5)

    end_date_label = tk.Label(right_frame, text="End Date:")
    end_date_label.grid(row=4, column=0, padx=10, pady=5, sticky="e")
    end_date_entry = tk.Entry(right_frame)
    end_date_entry.grid(row=4, column=1, padx=10, pady=5)

    # Generate button
    generate_button = tk.Button(right_frame, text="Generate Summary", command=lambda: generate_summary(
        pet_name_entry.get(),
        pet_weight_entry.get(),
        pet_type_var.get(),
        start_date_entry.get(),
        end_date_entry.get()
    ))
    generate_button.grid(row=5, column=0, columnspan=2, pady=10)

    return right_frame

# generate_summary.py

import tkinter as tk

def generate_summary(pet_name, pet_weight, pet_type, start_date, end_date):
    summary_window = tk.Toplevel()
    summary_window.title("Summary and Price Calculation")
    summary_window.geometry("400x300")

    # Summary content
    summary_label = tk.Label(summary_window, text=f"Pet Name: {pet_name}\nPet Weight: {pet_weight}\nPet Type: {pet_type}\nStart Date: {start_date}\nEnd Date: {end_date}")
    summary_label.pack(pady=10)

    # Close button
    close_button = tk.Button(summary_window, text="Close", command=summary_window.destroy)
    close_button.pack(pady=20)
