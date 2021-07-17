#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dados os valores n e k, gera as tabuadas de 
multiplicacao de n e de todos os seus antecessores
positivos, sendo que cada tabuada contem k linhas, 
inicando em zero.

@author: Prof. Diogo SM
"""

n = int(input("n: "))
k = int(input("k: "))

for i in range(n, 0, -1):
    for j in range(k):
        print(f"{i} * {j} = {i*j}")
    print()