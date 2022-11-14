from cryptography.fernet import Fernet
import getpass


with open('mykey.key', 'rb') as mykey:
    key = mykey.read()

print("Enter your name:")
name = input("> ")
if name == "Frank" or name == "John":
    print("Enter your password: ")
    password = getpass.getpass("> ")
    if password == "password":
        print("Enter file path: ")
        filepath = input("> ")
        f = Fernet(key)
        with open(filepath, 'rb') as encrypted_file:
            encrypted = encrypted_file.read()
            decrypted = f.decrypt(encrypted)
            newfile = filepath + 'decrypted.xlsx'
        with open(newfile, 'wb') as decrypted_file:
            decrypted_file.write(decrypted)
        print("File decrypted")
    else:
        print("wrong password")
else:
    print("Wrong username")
        