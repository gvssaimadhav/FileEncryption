import cryptography
import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
password_provided = "test_test"
password = password_provided.encode()
# For Generating a unique salt value:
# In the command shell: Enter the following commands
# import os
# To generate a 16bit key: os.urandom(16)
salt=b'\x96\x0f\xebx\xbdg\\\xec\x89t\x1e_c\xc7\x0b:'
kdf= PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
    )
key=base64.urlsafe_b64encode(kdf.derive(password)) # kdf can be used only once
#print(key)
# The Key Would be same everytime, because the password remains same.
# If we change the password, the generated key would also change.
# Storing the generated key on our system
file = open('generated_key.txt','wb')
file.write(key)
file.close()