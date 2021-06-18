#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Obriga o usuario a digitar um inteiro positivo, ou seja,
nao aceita a entrada enquanto um inteiro positivo nao
for digitado

@author: Prof. Diogo SM
"""
while True:
    n = int(input("Inteiro positivo: "))
    if n >= 0:
        break
print(n)

# code smell
#- duplicate code