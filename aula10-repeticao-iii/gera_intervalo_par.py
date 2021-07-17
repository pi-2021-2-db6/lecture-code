#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gera todos os inteiros pares de um intervalo, 
cujas extremidades sao entrada do programa.

@author: Prof. Diogo SM
"""
a = int(input("Inicio: "))
b = int(input("Fim: "))

a = a + 1 if a % 2 != 0 else a

for i in range(a, b + 1, 2):
    print(i, end=" ")
print()

