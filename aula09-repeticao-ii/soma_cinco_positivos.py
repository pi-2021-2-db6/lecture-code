#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Soma os primeiros cinco inteiros positivos digitados pelo 
usuario, ignorando os inteiros negativos da entrada.

@author: Prof. Diogo SM
"""

i = 0
s = 0

while i < 5:
    j = int(input("Inteiro positivo: "))
    
    if j >= 0:
        s = s + j
        i = i + 1
print(s)