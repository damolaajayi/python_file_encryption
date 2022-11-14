from cryptography.fernet import Fernet

with open('mykey.key', 'rb') as mykey:
    key = mykey.read()

#print(key)


f = Fernet(key)

with open('C:/Users/Hp840g5/Downloads/Test', 'rb') as original_file:
    original = original_file.read()


encrypted = f.encrypt(original)

with open ('C:/Users/Hp840g5/Downloads/Test_enc', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)