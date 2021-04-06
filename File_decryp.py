import cryptography
from cryptography.fernet import Fernet
# Read the Key From the file
file=open('generated_key.txt','rb')
key=file.read()
file.close()
# Decrypting the File:
# Open The file to Decrypt:
with open('password.txt.encrypted','rb') as f:
    data=f.read()
fernet=Fernet(key)
decrypted=fernet.decrypt(data)
# Writing the Encrypted File
with open('decrypted.txt','wb') as f:
    f.write(decrypted)