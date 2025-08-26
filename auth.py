# auth.py
from db_config import get_connection

def authenticate(username, password):
    connection = get_connection()
    cursor = connection.cursor()
    sql = "SELECT role FROM users WHERE username = ? AND password = ?"
    cursor.execute(sql, (username, password))
    result = cursor.fetchone()
    cursor.close()
    connection.close()
    if result:
        return result[0]  # role (admin or teacher)
    else:
        return None
