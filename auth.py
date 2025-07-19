
import hashlib
import sqlite3
import os

DB_PATH = 'fraud_detection_app/db/users.db'

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def create_user_table():
    os.makedirs('fraud_detection_app/db', exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT, role TEXT)")
    conn.commit()
    conn.close()

def add_user(username, password, role='analyst'):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('INSERT INTO users VALUES (?, ?, ?)', (username, hash_password(password), role))
    conn.commit()
    conn.close()

def verify_user(username, password):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE username = ? AND password = ?', 
              (username, hash_password(password)))
    user = c.fetchone()
    conn.close()
    return user
