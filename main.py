import os
from encryption import generate_key, load_key
from db import init_db, save_password, get_password, save_pm_login, get_pm_id

def main():
      if (not os.path.exists('key.key')):
            generate_key()
            print('Key generated!')
      
      key = load_key()
      init_db()
      print('Database initialized!')

      while True:
            print("\n Options: \n 1. Create a new login\n 2. Login to Password Manager\n 3. Exit\n")
            choice = input("Choose an option: ")
            if choice == '1':
                  pm_login_username = input("Enter a username for the manager: ")
                  pm_login_password = input("Enter a password for the manager: ")
                  save_pm_login(pm_login_username, pm_login_password, key)
                  pm_login_id = get_pm_id(pm_login_username, pm_login_password, key)

                  print(f"\nLogin created successfully as {pm_login_username}!")
            elif choice == '2':
                  pm_login_username = input("\nWhat user would you like to login to the manager as? ")
                  pm_login_password = input("Manager password: ")
                  pm_login_id = get_pm_id(pm_login_username, pm_login_password, key)

                  if pm_login_id is None:
                        print("\nInvalid username or password. Please try again.")
                        continue

                  print(f"\nLogged in successfully as {pm_login_username}!")
            elif choice == '3':
                  print("Exiting...")
                  continue
            else:
                  print("Invalid choice. Please try again.")
                  continue

            print("\nOptions:\n 1. Save Password\n 2. Retrieve Password\n 3. Exit\n")
            choice = input("Choose an option: ")

            if choice == '1':
                  website = input("Website: ")
                  username = input("Username: ")
                  password = input("Password: \n")
                  save_password(website, username, password, key)
                  print("Password saved!")
            elif choice == '2':
                  website = input("Website: ")
                  username, password = get_password(website, pm_login_id, key)
                  if username:
                        print(f"\nUsername: {username}, \nPassword: {password}")
                  else:
                        print("\nNo password found for that website.")
            elif choice == '3':
                  print("\nExiting...")
                  break
            else:
                  print("Invalid choice. Please try again.")
                  continue

if __name__ == "__main__":
      main()
