#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Testa os varios modos da funcao print
@author: Prof. Diogo SM
"""

# print com quebra de linha automatica
print("Ola mundo")
print("Ola ")
print("mundo")


# print com terminadores customizados
print("Ola", end="\n")
print()
print()
print()
print("mundo", end="")
print("novo")

# print com multiplos argumentos
print("Hello", "Diogo", "Martins", "how are you?", sep="#####$$$$$")
print("Nome", "Snome", "Idade", sep="\t")
print("Joao", "Silva", 23, sep="\t")
print("Maria", "Pedrosa", 31, sep="\t")

# strings formatadas
first_name = "Diogo"
last_name = "Martins"
age = 26
profession = "Professor"
affiliation = "UFABC"

print(first_name, last_name, age, profession, affiliation)
print(f"Hello, {first_name} {last_name}, you have {age} years old")
print(f"{first_name}, you are a {profession} and work at {affiliation}")
