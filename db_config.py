import pyodbc

def get_connection():
    connection = pyodbc.connect(
        'DRIVER={SQL Server};'
        'SERVER=DESKTOP-J7S23AB\\SQLEXPRESS;'
        'DATABASE=student_attendance;'
        'Trusted_Connection=yes;'
    )
    return connection
