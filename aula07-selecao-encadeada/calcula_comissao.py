#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Calcula a comissao do funcionario de acordo com a quantidade de produtos
vendidos pela empresa.

@author: Prof. Diogo SM
"""

p = int(input("Qtde de produtos: "))

if p >= 0:
    if p <= 250:
        v = p
    elif 250 <= p <= 500:
        v = p * 1.5
    elif p > 500:
        v = p * 2.0
    print(f"Comissao: R${v:.2f}")
else:
    print("Valor de comissao invalido")
