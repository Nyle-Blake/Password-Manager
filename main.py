import os
from encryption import generate_key, load_key
from db import init_db, save_password, get_password, save_pm_login, get_pm_id

def login_to_manager(key):
      print("\n Options: \n 1. Create a new login\n 2. Login to Password Manager\n")
      choice = input("Choose an option: ")
      if choice == '1':
            pm_login_username = input("Username: ")
            pm_login_password = input("Password: ")
            save_pm_login(pm_login_username, pm_login_password, key)
            pm_login_id = get_pm_id(pm_login_username, pm_login_password, key)

            print(f"\nLogin created successfully as {pm_login_username}!")
            return pm_login_id
      
      elif choice == '2':
            pm_login_username = input("\nUsername: ")
            pm_login_password = input("Password: ")
            pm_login_id = get_pm_id(pm_login_username, pm_login_password, key)

            if pm_login_id is None:
                  print("\nInvalid username or password. Please try again.")
                  return None
            
            print(f"\nLogged in successfully as {pm_login_username}!")
            return pm_login_id
      
      else:
            print("Invalid choice. Please try again.")
            return None

def choose_password(key, pm_login_id):
      print("\nOptions:\n 1. Save Password\n 2. Retrieve Password\n 3. Exit\n")
      choice = input("Choose an option: ")

      if choice == '1':
            website = input("Website: ")
            username = input("Username: ")
            password = input("Password: ")
            save_password(website, username, password, pm_login_id, key)
            print("\nPassword saved!")
            return None
      
      elif choice == '2':
            website = input("Website: ")
            username, password = get_password(website, pm_login_id, key)

            if username and password:
                  print(f"\nUsername: {username} \nPassword: {password}")
                  return password
            else:
                  print("\nNo password found for that website.")
                  return None
            
      elif choice == '3':
            print("\nExiting...")
            return 'Exit'
      
      else:
            print("Invalid choice. Please try again.")
            return None

def main():
      if (not os.path.exists('key.key')):
            generate_key()
            print('Key generated!')
      
      key = load_key()
      init_db()
      print('Database initialized!')

      while True:
            pm_login_id = login_to_manager(key)
            while pm_login_id is None:
                  pm_login_id = login_to_manager(key)
            
            password = choose_password(key, pm_login_id)
            while password is None:
                  password = choose_password(key, pm_login_id)

if __name__ == "__main__":
      main()
