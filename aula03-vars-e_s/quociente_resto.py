#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dado dois inteiros, calcula o quociente e o resto da divisao inteira
@author: Prof. Diogo SM
"""

dividendo = int(input("Dividendo: "))
divisor = int(input("Divisor: "))

quociente = dividendo // divisor
resto = dividendo % divisor

print(f"Quociente de {dividendo} / {divisor}: {quociente}")
print(f"Resto de {dividendo} / {divisor}: {resto}")

