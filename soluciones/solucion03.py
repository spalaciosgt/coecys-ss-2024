"""
Taller Desarrollo de Software Seguro
COECYS 2024
Ejercicio 03

Referencias:
OWASP Access Control Cheat Sheet
NIST SP 800-53: Security and Privacy Controls

Solución:
- Principio de Privilegio Mínimo
"""
def access_resource(user_role):
    roles = {"admin": ["resource1", "resource2"], "user": ["resource1"]}
    if user_role in roles:
        return f"Access to {', '.join(roles[user_role])} granted"
    else:
        return "Access denied"

user_role = input("Enter your role: ")
print(access_resource(user_role))