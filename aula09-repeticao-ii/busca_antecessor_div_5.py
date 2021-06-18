#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Busca o primeiro antecessor de n que seja divisivel por 5.

@author: Prof. Diogo SM
"""

n = int(input("n: "))
a = n - 1

while a > 0:
    if a % 5 == 0:
        break
    a -= 1

if a > 0:
    print(a)
else:
    print(f"Nao existe antecessor de {n} divisivel por 5")
    

# Exercicio:
# Dados os valores de n e k, encontrar o primeiro antecessor de 
# n que seja divisivel por k
