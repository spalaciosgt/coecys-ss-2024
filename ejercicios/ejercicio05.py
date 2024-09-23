"""
Taller Desarrollo de Software Seguro
COECYS 2024
Ejercicio 05

Referencias:
OWASP Code Review Guide - Static Code Analysis
"""

import subprocess

def run_command(command):
    subprocess.call(command, shell=True)

run_command("ls -la")