#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Determina o valor da dívida com base no capital, taxa de juros
e periodo transcorrido
@author: Prof. Diogo SM
"""

p = float(input("Capital (R$): "))
i = float(input("Taxa de juros (entre 0 e 1): "))
n = int(input("Periodo (em meses): "))

j = p * i * n
d = p + j

print(f"Divida: R${d:.2f}")
