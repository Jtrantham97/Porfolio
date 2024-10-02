# import statements
import secrets
import string
import json
from cryptography.fernet import Fernet

# generates an encryption key
def key_generating():
    key = Fernet.generate_key()
    with open ("secret_key", "wb") as key_files:
        key_files.write(key)

# will load the key
def loading_key():
    with open ("secret_key", "rb") as key_files:
        return key_files.read()

# encrypts password
def encrypt_password(password):
    key = loading_key()
    fern = Fernet(key)
    encrypted_password = fern.encrypt(password.encode())
    return encrypted_password

# decrypts password
def decrypt_password(encrypted_password):
    key = loading_key()
    fern = Fernet(key)
    decrypted_password = fern.decrypt(encrypted_password).decode()
    return decrypted_password

# saves the password to a file
def save_password(passwords):
    with open("passwords.json", "w" ) as file:
        json.dump(passwords, file)

# loads the saved password file
def load_password():
    try:
        with  open("passwords.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# creates a random password (WIP)
def random_password():
    special = ['@', '!', '&', '#', '$', '%', '*', '^']
    chars = string.ascii_letters + string.digits + ''.join(special)
    password_length = secrets.choice(range(14, 16))
    return ''.join(secrets.choice(chars) for _ in range(password_length))

def confirm_exit():
    exit_confirm = input("Are you sure you want to exit? Y/N ").strip().upper()
    if exit_confirm == "Y":
        print("Exiting...")
        return True
    elif exit_confirm == "N":
        print("Returning to menu...")
        return False
    else:
        print("Please enter Y/N to confirm exit")
        return confirm_exit()

def main():
    print("Starting...")
    # if needed, generates a key
    try:
        loading_key()
    except FileNotFoundError:
        print("key generated")
        return key_generating()
    
    passwords = load_password()

    while True:
        user_actions = input("What would you like to do? [add, get, delete, edit, exit]: ").strip().lower()
        if user_actions == "add":
            site = input("Site name: ")
            password = input("Enter password or have one made? [enter, make]: ").strip().lower()
            if password == "enter":
                password = input("Enter password: ")
                encrypted_password = encrypt_password(password)
                passwords[site] = encrypted_password.decode()
                save_password(passwords)
                print(f"Password for {site} has been created.")
            else:
                password = random_password()
                encrypted_password = encrypt_password(password)
                passwords[site] = encrypted_password.decode()
                save_password(passwords)
                print(f"password for {site} has been created.")
        
        elif user_actions == "get":
            site = input("Enter the site name: ")
            if site in passwords:
                decrypted_password = decrypt_password(passwords[site].encode())
                print(f"Password for {site} is {decrypted_password}.")
            else:
                print("No password found for that site.")

        elif user_actions == "delete":
            if site in passwords:
                del_confirm = print(input("Are you sure you want to delete the password for {site}? Y/N")).strip().upper()
                if del_confirm == "Y":
                   del passwords[site]
                   save_password[passwords]
                   print(f"Password for {site} has been deleted")
                elif del_confirm == "N":
                   print("Deletion has been canceled")
                else:
                   print("Invalid input. Please enter Y/N.")
            else:
                print(f"No password for {site} found.")
        elif user_actions == "edit":
            if site in passwords:
                site = input("Please enter site you wish to edit ")
                new_pass = input("Enter new password for {site}: ")
                passwords[site] = encrypt_password(new_pass)
                save_password[passwords]
                print(f"The password has been updated for {site}")
            else:
                createnew = input(f"No password found for site. Would you like to create one? Y/N").strip().upper()
                if createnew == "Y":
                    new_pass = input("Please enter password for {site} ")
                    passwords[site] = encrypt_password(new_pass)
                    save_password[passwords]
                    print(f"Password for {site} has been created successfully")
                elif createnew == "N":
                    print("No changes made ")
                else:
                    print("invalid input please enter Y/N ")
        elif user_actions == "exit":
            if confirm_exit():
                break 
            else:
                return main()

        else:
            print("Please enter a valid response. [add, get, delete, edit, exit]")


if __name__ == "__main__":
    main()
