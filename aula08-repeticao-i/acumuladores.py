#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exibe exemplos de acumuladores.

@author: Prof. Diogo SM
"""

v1 = 10
v2 = 20
v3 = 30
acumulador = 0

acumulador += v1
print(acumulador)
acumulador += v2
print(acumulador)
acumulador += v3
print(acumulador)

acumulador = 0
i = 0

while i < 5:
    v = int(input("digite um int: "))
    acumulador += v
    i += 1
print(acumulador)