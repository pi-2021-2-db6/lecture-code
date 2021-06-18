#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Imprime a tabuada de potenciacao de n, com k linhas.

@author: Prof. Diogo SM
"""
n = int(input("n: "))
k = int(input("k: "))

i = 0

while i < k:
    print(f"{n}**{i} = {n**i}")
    i += 1
