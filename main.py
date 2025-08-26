# main.py
import tkinter as tk
from tkinter import messagebox, font
from PIL import Image, ImageTk
from auth import authenticate
from student import add_student_gui
from attendance import record_attendance_gui
from reports import generate_report_gui, show_trends_gui

# Global variable to track root window (for logout)
root = None

def launch_main_menu(user_role, username):
    global root
    root = tk.Tk()
    root.title("Student Attendance Management System")
    root.geometry("600x500")

    try:
        bg_image = Image.open("assets/background_login.jpg")
        bg_image = bg_image.resize((600, 500), Image.Resampling.LANCZOS)
        bg_photo = ImageTk.PhotoImage(bg_image)

        bg_label = tk.Label(root, image=bg_photo)
        bg_label.image = bg_photo
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    except Exception as e:
        print("Could not load background image:", e)
        root.configure(bg="#f0f8ff")

    title_font = font.Font(family="Helvetica", size=18, weight="bold", slant="italic")
    button_font = font.Font(family="Arial", size=12, weight="bold")

    # Title
    title_label = tk.Label(root, text="Student Attendance Management System", font=title_font, fg="#2e8b57")
    title_label.place(relx=0.5, rely=0.1, anchor="center")

    # Welcome message
    welcome_label = tk.Label(root, text=f"Welcome {username}", font=('Arial', 14, 'bold'), fg="#000080")
    welcome_label.place(relx=0.5, rely=0.2, anchor="center")

    # Buttons
    y_start = 0.35
    spacing = 0.08

    tk.Button(root, text="Add Student", width=25, font=button_font, bg="#ffcccb", fg="black", command=add_student_gui).place(relx=0.5, rely=y_start, anchor="center")
    tk.Button(root, text="Record Attendance", width=25, font=button_font, bg="#add8e6", fg="black", command=record_attendance_gui).place(relx=0.5, rely=y_start + spacing, anchor="center")
    tk.Button(root, text="View Attendance Report", width=25, font=button_font, bg="#90ee90", fg="black", command=generate_report_gui).place(relx=0.5, rely=y_start + spacing * 2, anchor="center")

    if user_role == "admin":
        tk.Button(root, text="Show Attendance Trends", width=25, font=button_font, bg="#ffd700", fg="black", command=show_trends_gui).place(relx=0.5, rely=y_start + spacing * 3, anchor="center")

    tk.Button(root, text="Logout", width=25, font=button_font, bg="#ffa07a", fg="black", command=logout).place(relx=0.5, rely=y_start + spacing * 4.2, anchor="center")

    root.mainloop()

def logout():
    global root
    if root is not None:
        root.destroy()
        login_screen()

def login_screen():
    login_window = tk.Tk()
    login_window.title("Login - Student Attendance Management System")
    login_window.geometry("600x400")

    try:
        # Load background image
        bg_image = Image.open("assets/background_login.jpg")
        bg_image = bg_image.resize((600, 400), Image.Resampling.LANCZOS)
        bg_photo = ImageTk.PhotoImage(bg_image)

        bg_label = tk.Label(login_window, image=bg_photo)
        bg_label.image = bg_photo
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    except Exception as e:
        print("Could not load background image:", e)
        login_window.configure(bg="#f0f8ff")

    # Title smaller font
    title_font = font.Font(family="Helvetica", size=16, weight="bold", slant="italic")
    title_label = tk.Label(login_window, text="Student Attendance Management System", font=title_font, fg="#2e8b57")
    title_label.place(relx=0.5, rely=0.1, anchor="center")

    # Load and place user logo image
    try:
        user_logo_image = Image.open("assets/user_logo.jpg")
        user_logo_image = user_logo_image.resize((80, 80), Image.Resampling.LANCZOS)
        user_logo_photo = ImageTk.PhotoImage(user_logo_image)

        user_logo_label = tk.Label(login_window, image=user_logo_photo)
        user_logo_label.image = user_logo_photo
        user_logo_label.place(relx=0.5, rely=0.25, anchor="center")
    except Exception as e:
        print("Could not load user logo image:", e)

    # Username label + entry
    tk.Label(login_window, text="Username:", font=('Arial', 12, 'bold'), fg="black").place(relx=0.3, rely=0.45, anchor="e")
    username_entry = tk.Entry(login_window, font=('Arial', 12))
    username_entry.place(relx=0.4, rely=0.45, anchor="w")

    # Password label + entry
    tk.Label(login_window, text="Password:", font=('Arial', 12, 'bold'), fg="black").place(relx=0.3, rely=0.55, anchor="e")
    password_entry = tk.Entry(login_window, font=('Arial', 12), show="*")
    password_entry.place(relx=0.4, rely=0.55, anchor="w")

    # Login button
    def do_login():
        username = username_entry.get()
        password = password_entry.get()
        role = authenticate(username, password)
        if role:
            messagebox.showinfo("Login Success", f"Welcome, {username}! Role: {role}")
            login_window.destroy()
            launch_main_menu(role, username)
        else:
            messagebox.showerror("Login Failed", "Invalid credentials!")

    tk.Button(login_window, text="Login", font=('Arial', 12, 'bold'), bg="#32cd32", fg="white", command=do_login).place(relx=0.5, rely=0.68, anchor="center")

    login_window.mainloop()

# Start the app with login screen
if __name__ == "__main__":
    login_screen()
