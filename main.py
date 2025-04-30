import os
from encryption import generate_key, load_key
from db import init_db, save_password, get_password

def main():
      if (not os.path.exists('key.key')):
            generate_key()
            print('Key generated!')
      
      key = load_key()
      init_db()
      print('Database initialized!')

      while True:
            print("\nOptions: 1. Save Password 2. Retrieve Password 3. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                  website = input("Website: ")
                  username = input("Username: ")
                  password = input("Password: ")
                  save_password(website, username, password, key)
                  print("Password saved!")
            elif choice == '2':
                  website = input("Website: ")
                  username, password = get_password(website, key)
                  if username:
                        print(f"\nUsername: {username}, Password: {password}")
                  else:
                        print("\nNo password found for that website.")
            elif choice == '3':
                  print("\nExiting...")
                  break

if __name__ == "__main__":
      main()
