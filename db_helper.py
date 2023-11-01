# db_helper.py
import sqlite3

def create_table():
    with sqlite3.connect("users.db") as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users 
                          (username TEXT PRIMARY KEY, password TEXT)''')

def insert_user(username, password):
    with sqlite3.connect("users.db") as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))

def get_user(username):
    with sqlite3.connect("users.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        return cursor.fetchone()
