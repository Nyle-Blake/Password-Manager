import sqlite3
from encryption import encrypt_message, decrypt_message

def init_db():
      conn = sqlite3.connect('passwords.db')
      cursor = conn.cursor()
      cursor.execute('''CREATE TABLE IF NOT EXISTS passwords
                        (website TEXT PRIMARY KEY, username TEXT, password TEXT)''')
      conn.commit()
      conn.close()

def save_password(website, username, password, key):
      encrypted_password = encrypt_message(password, key)
      conn = sqlite3.connect('passwords.db')
      cursor = conn.cursor()
      cursor.execute('INSERT OR REPLACE INTO passwords (website, username, password) VALUES (?, ?, ?)', (website, username, encrypted_password))
      conn.commit()
      conn.close()

def get_password(website, key):
      conn = sqlite3.connect('passwords.db')
      cursor = conn.cursor()
      cursor.execute('SELECT username, password FROM passwords WHERE website = ?', (website,))
      result = cursor.fetchone()
      conn.close()
      if result:
            username, encrypted_password = result
            decrypted_password = decrypt_message(encrypted_password, key)
            return username, decrypted_password
      return None, None