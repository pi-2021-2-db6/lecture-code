#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Imprime uma progressao aritmetica com base nos valores do 
termo inicial, da diferenca entre os termos (passo) e da 
quantidade de termos.

@author: Prof. Diogo SM
"""
a = int(input("Primeiro termo: "))
p = int(input("Diferenca (ou passo): "))
k = int(input("Qtde. de termos: "))

i = 0

while i < k:
    print(a, end=" ")
    i = i + 1
    a = a + p
print()

