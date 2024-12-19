import hashlib
import getpass

password_manager = {}

def create_account():
    username = input("Enter your name:")
    password = getpass.getpass("Enter your password") 
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    password_manager[username]= hashed_password
    print("Account created successfully")
    
def login():
    username = input("Enter your name:")
    password = getpass.getpass("Enter your password") 
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    if username in password_manager and password_manager[username] == hashed_password:
     print("Login successful")
    else:
     print("Invalid username or password")

def main():
   while True:
      choice = input(" enter 1 to create account and 2 to login:")
      if choice =="1":
         create_account()
      elif choice == "2":
         login()
      else:
         print("Invalid choice")

if __name__=="__main__":
   main()