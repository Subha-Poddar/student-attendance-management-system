# reports.py
from db_config import get_connection
import tkinter as tk
from tkinter import ttk, filedialog
import csv
import matplotlib.pyplot as plt

def generate_report_gui():
    window = tk.Toplevel()
    window.title("Attendance Report")

    tree = ttk.Treeview(window, columns=("First Name", "Last Name", "Date", "Status"), show="headings")
    tree.heading("First Name", text="First Name")
    tree.heading("Last Name", text="Last Name")
    tree.heading("Date", text="Date")
    tree.heading("Status", text="Status")
    tree.pack()

    connection = get_connection()
    cursor = connection.cursor()
    sql = """
    SELECT s.first_name, s.last_name, CONVERT(VARCHAR, a.date, 23) as date, a.status
    FROM attendance a
    JOIN students s ON a.student_id = s.student_id
    ORDER BY a.date DESC
    """
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        flat_row = [str(col) for col in row]
        tree.insert("", tk.END, values=flat_row)

    cursor.close()
    connection.close()

    def export_csv():
        file_path = filedialog.asksaveasfilename(defaultextension=".csv")
        if file_path:
            with open(file_path, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["First Name", "Last Name", "Date", "Status"])
                for row_id in tree.get_children():
                    row = tree.item(row_id)['values']
                    writer.writerow(row)

    tk.Button(window, text="Export to CSV", command=export_csv).pack()

def show_trends_gui():
    connection = get_connection()
    cursor = connection.cursor()

    sql = """
    SELECT 
        COUNT(CASE WHEN status='Present' THEN 1 END) AS present_count,
        COUNT(CASE WHEN status='Absent' THEN 1 END) AS absent_count
    FROM attendance
    """
    cursor.execute(sql)
    result = cursor.fetchone()

    cursor.close()
    connection.close()

    present_count = result[0] or 0
    absent_count = result[1] or 0

    counts = [present_count, absent_count]
    labels = ['Present', 'Absent']

    plt.figure(figsize=(8,8))
    plt.pie(
        counts, labels=labels,
        autopct='%1.1f%%',
        startangle=140,
        colors=["#1460A7", "#837A79"],
        textprops={'color': 'black', 'fontsize': 14}
    )
    plt.title('Overall Attendance Distribution')
    plt.axis('equal')
    plt.show()
