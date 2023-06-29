'''
Write A Python Program To Check Whether 
Username Is Encrypted Form Or Not
'''

import hashlib

def check_encrypted(username, encrypted_username, encryption_method):
    if encryption_method == 'md5':
        encrypted = hashlib.md5(username.encode()).hexdigest()
    elif encryption_method == 'sha256':
        encrypted = hashlib.sha256(username.encode()).hexdigest()

    return encrypted == encrypted_username

if __name__=="__main__":
    username = input("Enter the username: ")
    encrypted_username = input("Enter the encrypted username: ")
    encryption_method = input("Enter the encryption method (md5, sha256): ")

    if check_encrypted(username, encrypted_username, encryption_method):
        print("The username is in encrypted form.")
    else:
        print("The username is not in encrypted form or does not match the given encryption method.")
