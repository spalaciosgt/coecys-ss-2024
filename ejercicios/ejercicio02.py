"""
Taller Desarrollo de Software Seguro
COECYS 2024
Ejercicio 02

Referencias:
OWASP Secure Coding Practices - Data Protection
NIST SP 800-57: Recommendation for Key Management
"""

def store_user_data(username, password):
    with open("user_data.txt", "a") as f:
        f.write(f"{username}:{password}\n")

username = input("Enter username: ")
password = input("Enter password: ")
store_user_data(username, password)