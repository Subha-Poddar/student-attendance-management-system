# student.py
from db_config import get_connection
import tkinter as tk
from tkinter import messagebox

def add_student_gui():
    def submit_student():
        first_name = entry_first_name.get()
        last_name = entry_last_name.get()
        roll_number = entry_roll_number.get()
        class_name = entry_class.get()

        connection = get_connection()
        cursor = connection.cursor()
        sql = "INSERT INTO students (first_name, last_name, roll_number, class) VALUES (?, ?, ?, ?)"
        val = (first_name, last_name, roll_number, class_name)
        cursor.execute(sql, val)
        connection.commit()
        cursor.close()
        connection.close()

        messagebox.showinfo("Success", "Student added successfully!")
        window.destroy()

    window = tk.Toplevel()
    window.title("Add Student")
    window.configure(bg="#f0f8ff")

    tk.Label(window, text="First Name", bg="#f0f8ff", font=('Arial', 12, 'bold')).grid(row=0, column=0)
    tk.Label(window, text="Last Name", bg="#f0f8ff", font=('Arial', 12, 'bold')).grid(row=1, column=0)
    tk.Label(window, text="Roll Number", bg="#f0f8ff", font=('Arial', 12, 'bold')).grid(row=2, column=0)
    tk.Label(window, text="Class", bg="#f0f8ff", font=('Arial', 12, 'bold')).grid(row=3, column=0)

    entry_first_name = tk.Entry(window, font=('Arial', 12))
    entry_last_name = tk.Entry(window, font=('Arial', 12))
    entry_roll_number = tk.Entry(window, font=('Arial', 12))
    entry_class = tk.Entry(window, font=('Arial', 12))

    entry_first_name.grid(row=0, column=1)
    entry_last_name.grid(row=1, column=1)
    entry_roll_number.grid(row=2, column=1)
    entry_class.grid(row=3, column=1)

    tk.Button(window, text="Submit", font=('Arial', 12, 'bold'), bg="#32cd32", fg="white", command=submit_student).grid(row=4, column=0, columnspan=2, pady=10)


