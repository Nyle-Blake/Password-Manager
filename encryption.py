from cryptography.fernet import Fernet

def generate_key():
      key = Fernet.generate_key()
      with open('key.key', 'wb') as key_file:
          key_file.write(key)

def load_key():
      return open('key.key', 'rb').read()

def encrypt_message(message, key):
     return Fernet(key).encrypt(message.encode()).decode()

def decrypt_message(token, key):
     return Fernet(key).decrypt(token.encode()).decode()
