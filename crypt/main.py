from cryptography.fernet import Fernet



def create_key(): # create a key for encrypted file
    key = Fernet.generate_key()

    with open("crypto.key", 'wb') as key_file:
        key_file.write(key)   # save key in some file

def load_key(): # get key for encrypted file
    return open('crypto.key', 'rb').read()


def encrypt(filename, key): #fucntion of encrypt
    f = Fernet(key)

    with open(filename, 'rb') as file: # open and read data in encrypted file
        file_data = file.read()

    encrypted_data = f.encrypt(file_data) # encrypt data in file


    with open(filename, 'wb') as file: # opne file with data and encrypt
        file.write(encrypted_data)

def decrypt(filename, key): # function of decrypt
    f = Fernet(key)

    with open(filename, 'rb') as enc_file: # open and read file with encrypted data
        encryptted = enc_file.read()

    decrypted = f.decrypt(encryptted) # decrypt data

    with open(filename, 'wb') as dec_file: # write decrypted data in file
        dec_file.write(decrypted)

filename = './crypt/text.txt' # path to file
key = load_key() # get key

try:
    #encrypt(filename, key)
    decrypt(filename, key)
except:
    create_key()
    #encrypt(filename, key)
    decrypt(filename, key)
