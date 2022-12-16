from cryptography.fernet import Fernet



def create_key():
    key = Fernet.generate_key()

    with open("crypto.key", 'wb') as key_file:
        key_file.write(key)

def load_key():
    return open('crypto.key', 'rb').read()


def encrypt(filename, key):
    f = Fernet(key)

    with open(filename, 'rb') as file:
        file_data = file.read()

    encrypted_data = f.encrypt(file_data)


    with open(filename, 'wb') as file:
        file.write(encrypted_data)

def decrypt(filename, key):
    f = Fernet(key)

    with open(filename, 'rb') as enc_file:
        encryptted = enc_file.read()

    decrypted = f.decrypt(encryptted)

    with open(filename, 'wb') as dec_file:
        dec_file.write(decrypted)

filename = './crypt/text.txt'
key = load_key()

try:
    #encrypt(filename, key)
    decrypt(filename, key)
except:
    create_key()
    #encrypt(filename, key)
    decrypt(filename, key)
