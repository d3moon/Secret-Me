import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def obfuscate_payload(password):
    filepath = input("Enter the filepath of the payload: ")
    if not os.path.isfile(filepath):
        print("[ERROR] The file does not exist.")
        return None

    with open(filepath, 'rb') as f:
        payload = f.read()

    salt = os.urandom(16)

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256,
        iterations=100000,
        length=32,
        salt=salt,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))

    fernet = Fernet(key)
    encrypted_payload = fernet.encrypt(payload)

    new_filepath = filepath + '.enc'
    with open(new_filepath, 'wb') as f:
        f.write(salt + encrypted_payload)
    print("File successfully encrypted and stored at {}".format(new_filepath))
    return salt, encrypted_payload

password = b'password'
encryption_result = obfuscate_payload(password)
if encryption_result:
    salt, obfuscated_payload = encryption_result
    print(salt)
    print(obfuscated_payload)
else:
    print("Encryption failed.")


