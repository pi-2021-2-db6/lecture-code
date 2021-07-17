#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dados os valores de n e k, gera a tabuada de 
multiplicacao de n com k linhas.

@author: Prof. Diogo SM
"""

n = int(input("n: "))
k = int(input("k: "))
m = 0

while m < k:
    print(f"{n} * {m} = {n*m}")
    m = m + 1

