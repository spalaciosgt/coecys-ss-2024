"""
Taller Desarrollo de Software Seguro
COECYS 2024
Ejercicio 04

Referencias:
OWASP Code Review Guide - Code Obfuscation
NIST SP 800-95: Guide to Secure Web Services (incluye prácticas sobre protección del código)
"""

def greet(name):
    print(f"Hello, {name}!")

name = input("Enter your name: ")
greet(name)