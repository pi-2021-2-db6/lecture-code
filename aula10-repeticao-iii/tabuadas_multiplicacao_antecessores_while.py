#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dados os valores n e k, gera as tabuadas de 
multiplicacao de n e de todos os seus antecessores
positivos, sendo que cada tabuada contem k linhas, 
indicando em zero.

@author: Prof. Diogo SM
"""

n = int(input("n: "))
k = int(input("k: "))

i = n
while i > 0:
    j = 0
    while j < k:
        print(f"{i} * {j} = {i*j}")
        j = j + 1
    print()
    i = i - 1