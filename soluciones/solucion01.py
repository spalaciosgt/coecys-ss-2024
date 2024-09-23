"""
Taller Desarrollo de Software Seguro
COECYS 2024
Solución 01

Referencias:
OWASP Secure Coding Practices - Validation
NIST SP 800-63B: Digital Identity Guidelines

Solución:
- Aplicación de Hashing
- Ocultación de ingreso del Password
- Aplicar Sanitización a parámetros (tal vez sea necesario instalar pip install cerberus, pip install validators)
"""

import hashlib
import getpass
from cerberus import Validator

def hash_password(password): 
    return hashlib.sha256(password.encode()).hexdigest()

def login(username, password):
    username = sanitizar_username(username)
    password = sanitizar_password(password)
    stored_password = hash_password("P@ssword$23")
    if username == "admin" and hash_password(password) == stored_password:
        return "Access granted"
    else:
        return "Access denied"

def sanitizar_username(username):
    schema = {'username': {'type': 'string', 'minlength': 1, 'maxlength': 20, 'regex': '^[a-zA-Z0-9_]*$'}}
    v = Validator(schema)    
    if v.validate({'username': username}):
        return username
    else:
        return None

def sanitizar_password(password):
    schema = {
        'password': {
            'type': 'string',
            'minlength': 8,
            'regex': '^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[!@#$%^&*(),.?":{}|<>]).*$'
        }
    }
    v = Validator(schema)    
    if v.validate({'password': password}):
        return password
    else:
        return None

username = input("Enter username: ")
print("Enter password: ", end="")
password = getpass.getpass()
print(login(username, password))