import sqlite3
import hashlib
from encryption import encrypt_message, decrypt_message

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def init_db():
      conn = sqlite3.connect('passwords.db')
      cursor = conn.cursor()
      cursor.execute('''CREATE TABLE IF NOT EXISTS passwords
                        (website TEXT PRIMARY KEY, username TEXT, password TEXT, login_id INTEGER,
                        FOREIGN KEY (login_id) REFERENCES logins(id))''')
      # cursor.execute('''DROP TABLE IF EXISTS logins''')  # Ensure the table is fresh
      cursor.execute('''CREATE TABLE IF NOT EXISTS logins
                        (id INTEGER PRIMARY KEY, username TEXT, password TEXT, password_hash TEXT)''')
      conn.commit()
      conn.close()

def save_password(website, username, password, pm_login_id, key):
      encrypted_password = encrypt_message(password, key)
      conn = sqlite3.connect('passwords.db')
      cursor = conn.cursor()
      cursor.execute('INSERT OR REPLACE INTO passwords (website, username, password, login_id) VALUES (?, ?, ?, ?)', (website, username, encrypted_password, pm_login_id))
      conn.commit()
      conn.close()

def get_password(website, pm_login_id, key):
      conn = sqlite3.connect('passwords.db')
      cursor = conn.cursor()
      cursor.execute('SELECT username, password FROM passwords WHERE website = ? AND login_id = ?', (website, pm_login_id))
      result = cursor.fetchone()
      conn.close()
      if result:
            username, encrypted_password = result
            decrypted_password = decrypt_message(encrypted_password, key)
            return username, decrypted_password
      return None, None

def save_pm_login(username, password, key):
      encrypted_password = encrypt_message(password, key)  # For storage
      password_hash = hash_password(password) #For lookup
      conn = sqlite3.connect('passwords.db')
      cursor = conn.cursor()
      cursor.execute('INSERT OR REPLACE INTO logins (username, password, password_hash) VALUES (?, ?, ?)', (username, encrypted_password, password_hash))
      conn.commit()
      conn.close()

def get_pm_id(username, password, key):
      password_hash = hash_password(password)
      conn = sqlite3.connect('passwords.db')
      cursor = conn.cursor()
      cursor.execute('SELECT id FROM logins WHERE username = ? AND password_hash = ?', (username, password_hash))
      result = cursor.fetchone()
      conn.close()
      if result:
            return result[0]
      return None