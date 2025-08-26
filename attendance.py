# attendance.py
from db_config import get_connection
import tkinter as tk
from tkinter import messagebox
import datetime

def record_attendance_gui():
    def submit_attendance():
        selected_index = student_listbox.curselection()
        if not selected_index:
            messagebox.showwarning("Selection Error", "Please select a student.")
            return

        selected_student_id = student_ids[selected_index[0]]
        status = status_var.get()

        connection = get_connection()
        cursor = connection.cursor()
        
        # Use ? placeholders for SQL Server with pyodbc
        sql = "INSERT INTO attendance (student_id, date, status) VALUES (?, ?, ?)"
        val = (selected_student_id, datetime.date.today().strftime('%Y-%m-%d'), status)
        
        try:
            cursor.execute(sql, val)
            connection.commit()
            messagebox.showinfo("Success", "Attendance recorded successfully!")
            window.destroy()
        except Exception as e:
            messagebox.showerror("Database Error", str(e))
        finally:
            cursor.close()
            connection.close()

    window = tk.Toplevel()
    window.title("Record Attendance")

    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT student_id, first_name, last_name FROM students")
    students = cursor.fetchall()
    cursor.close()
    connection.close()

    student_ids = []
    student_names = []
    for s in students:
        student_ids.append(s[0])
        student_names.append(f"{s[1]} {s[2]}")

    tk.Label(window, text="Select Student").pack()
    student_listbox = tk.Listbox(window)
    for name in student_names:
        student_listbox.insert(tk.END, name)
    student_listbox.pack()

    tk.Label(window, text="Status").pack()
    status_var = tk.StringVar(value="Present")
    tk.Radiobutton(window, text="Present", variable=status_var, value="Present").pack()
    tk.Radiobutton(window, text="Absent", variable=status_var, value="Absent").pack()

    tk.Button(window, text="Submit Attendance", command=submit_attendance).pack()
