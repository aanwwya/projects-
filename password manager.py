# password manager 

from cryptography.fernet import Fernet
import os
MASTER_PASSWORD = "1234"

if not os.path.exists("passwords.txt"):
    open("passwords.txt", "w").close()


def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    with open("key.key", "rb") as file:
        return file.read()

if not os.path.exists("key.key"):
    write_key()

key = load_key()
fer = Fernet(key)

master_pwd = input("Enter master password: ")

if master_pwd != MASTER_PASSWORD:
    print("Access denied!")
    quit()


def check_strength(password):
    if len(password) < 6:
        return "Weak"
    elif password.isalpha() or password.isdigit():
        return "Medium"
    else:
        has_upper = False
        has_lower = False
        has_digit = False
        has_symbol = False
        for char in password:
            if char.isupper():
                has_upper = True
            elif char.islower():
                has_lower = True
            elif char.isdigit():
                has_digit = True
            else:
                has_symbol = True
        if has_upper and has_lower and has_digit and has_symbol:
            return "Strong"
        else:
            return "Medium"

def view():
    with open('passwords.txt','r') as f:
        for line in f:
            data=line.strip()
            if "|" in data:
                try:
                    user,passw=data.split("|")
                    print("User:",user,"Password:",fer.decrypt(passw.encode()).decode())
                except:
                    print("Error decrypting entry:",data)

def search():
    account=input("Enter account name: ")
    found=False
    with open('passwords.txt','r') as f:
        for line in f:
            data=line.rstrip()
            if "|" in data:
                try:
                    user,passw=data.split("|")
                    if user==account:
                        print("User:",user,"Password:",fer.decrypt(passw.encode()).decode())
                        found=True
                except:
                    pass
    if not found:
        print("account not found!")
        
        
def delete():
    account=input("Enter account name to delete: ")
    lines=[]
    with open("passwords.txt","r") as f:
        lines=f.readlines()
    with open("passwords.txt","w") as f:
        found=False
        for line in lines:
            data=line.rstrip()
            if "|" in data:
                user,passw=data.split("|")
                if user!=account:
                    f.write(line)
                else:
                    found=True
            else:
                f.write(line)
    if found:
        print("Account deleted successfully.")
    else:
        print("Account not found.")
        
def add():
    name = input('Account Name: ')
    pwd = input("Password: ")
    strength = check_strength(pwd)
    print("Password Strength:", strength)
    
    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
 mode = input(" would you like to add a new password or view existing ones(view,add,search), press q to quit ").lower()
 if mode == "q":
     break
     
 if mode == "view":
    view()
 elif mode == 'add':
    add()
 elif mode == 'search':
      search()
 else:
    print("invalid mode.")
print("Program closed.")
    
    
# this program stores passwords securely using encryption.
# features:
# - add new passwords
# - save encrypted passwords in a file
# - view and decrypt saved passwords

# fernet encryption converts passwords into unreadable text for security

# a secret key stored in key.key is used for both encryption and decryption.

# instructions:
# - type "add" to save a new password
# - type "view" to see saved passwords
# - type "q" to quit the program
