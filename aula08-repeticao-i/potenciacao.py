#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Calcula a operacao de potenciacao, considerando 
base inteira e expoente inteiro positivo ou nulo.

@author: Prof. Diogo SM
"""

base = int(input("Base: "))
expoente = int(input("Expoente: "))

contador = 0
potencia = 1

while contador < expoente:
    potencia = potencia * base
    contador = contador + 1
print(potencia)

