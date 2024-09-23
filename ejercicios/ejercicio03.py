"""
Taller Desarrollo de Software Seguro
COECYS 2024
Ejercicio 03

Referencias:
OWASP Access Control Cheat Sheet
NIST SP 800-53: Security and Privacy Controls
"""

def access_resource(user_role):
    if user_role == "admin":
        return "Access to the resource granted"
    else:
        return "Access denied"

user_role = input("Enter your role: ")
print(access_resource(user_role))