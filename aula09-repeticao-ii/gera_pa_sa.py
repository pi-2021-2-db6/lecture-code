#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Imprime uma progressao aritmetica e o valor da serie
aritmetica com base nos valores do 
termo inicial, da diferenca entre os termos (passo) e da 
quantidade de termos.

@author: Prof. Diogo SM
"""
a0 = int(input("Primeiro termo: "))
p = int(input("Diferenca (ou passo): "))
k = int(input("Qtde. de termos: "))

i = 0
a = a0

while i < k:
    print(a, end="")
    if i < k - 1:
        print(",", end=" ")
    i = i + 1
    a = a + p
print()

a = a0
i = 0
s = 0

while i < k:
    print(a, end=" ")
    s = s + a
    if i < k - 1:
        print("+", end=" ")
    i = i + 1
    a = a + p
print("=", s)

