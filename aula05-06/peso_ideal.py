#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Calcula o peso ideal com base no sexo e na altura
@author: Prof. Diogo SM
"""

altura = float(input("Altura (m): "))
sexo = input("Sexo (m|f): ")

if sexo == "m" or sexo == "f":
    if sexo == "m":
        peso = 72.7 * altura - 58
    else:
        peso = 62.1 * altura - 44.7
        
    print(f"Peso ideal: {peso:.3f}kg")
else:
    print("Valor de sexo invalido")
    


