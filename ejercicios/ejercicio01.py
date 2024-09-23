"""
Taller Desarrollo de Software Seguro
COECYS 2024
Ejercicio 01

Referencias:
OWASP Secure Coding Practices - Validation
NIST SP 800-63B: Digital Identity Guidelines
"""

def login(username, password):
    if username == "admin" and password == "P@ssword$23":
        return "Access granted"
    else:
        return "Access denied"

username = input("Enter username: ")
password = input("Enter password: ")
print(login(username, password))