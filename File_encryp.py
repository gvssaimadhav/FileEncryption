import cryptography
from cryptography.fernet import Fernet
# Read the Key From the file
file=open('generated_key.txt','rb')
key=file.read()
file.close()
# Encrypt the File:
# Open The file to Encrypt:
with open('password.txt','rb') as f:
    data=f.read()
    fernet=Fernet(key)
    encrypted=fernet.encrypt(data)
# Writing the Encrypted File
with open('password.txt.encrypted','wb') as f:
    f.write(encrypted)