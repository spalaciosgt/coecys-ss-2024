"""
Taller Desarrollo de Software Seguro
COECYS 2024
Ejercicio 02

Referencias:
OWASP Secure Coding Practices - Data Protection
NIST SP 800-57: Recommendation for Key Management

Solución:
- Aplicación de un cifrado simétrico con una llave
"""

import getpass
from cryptography.fernet import Fernet
import os

def save_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("secret.key", "rb").read()

def encrypt_data(data, cipher_suite):
    return cipher_suite.encrypt(data.encode())

def store_user_data(username, password):
    cipher_suite = Fernet(load_key())    
    try:
        with open("user_data.enc", "ab") as f:
            encrypted_username = encrypt_data(username, cipher_suite)
            encrypted_password = encrypt_data(password, cipher_suite)
            f.write(encrypted_username + b":" + encrypted_password + b"\n")
    except Exception as e:
        print(f"Error al almacenar datos: {e}")

def decrypt_data(encrypted_data, cipher_suite):
    return cipher_suite.decrypt(encrypted_data).decode()

if not os.path.exists("secret.key"):
    save_key()

# Solicitar el nombre de usuario y la contraseña
username = input("Enter username: ")
print("Enter password: ", end="")
password = getpass.getpass()

store_user_data(username, password)
print("User data stored successfully.")

"""
encrypted_data = None
cipher_suite = Fernet(load_key())  
print(decrypt_data(encrypted_data, cipher_suite))
"""