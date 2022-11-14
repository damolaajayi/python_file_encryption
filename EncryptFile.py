from cryptography.fernet import Fernet
import getpass
from datetime import datetime

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

with open('mykey.key', 'rb') as mykey:
    key = mykey.read()
print("Enter your name:")
name = input("> ")

if name == "Frank" or name == "John":
    print("Enter your password: ")
    #print(name + 'doe')
    password = getpass.getpass("> ")
    if password == "password":
        print("Enter file path: ")
        filepath = input("> ")
        f = Fernet(key)
        with open(filepath, 'rb') as original_file:
            original = original_file.read()
            encrypted = f.encrypt(original)
        newfile = filepath + 'encrypted.xlsx'
        with open (newfile, 'wb') as encrypted_file:
            encrypted_file.write(encrypted)
        print("File encrypted")
    else:
        print("wrong password")
else:
    print("Wrong username")