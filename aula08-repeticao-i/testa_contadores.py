#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exibe varios padroes de contadores.

@author: Prof. Diogo SM
"""

contador = 0

print("10 iteracoes com passo 1")
while contador < 10:
    print(contador, end=" ")
    contador +=  1
print()

contador = 0
    
print("11 iteracoes com passo 1")
while contador <= 10:
    print(contador, end=" ")
    contador += 1
print()

contador = 1
    
print("30 iteracoes com passo 1")
while contador < 30:
    print(contador, end=" ")
    contador += 1
print()

contador = 10

print("10 iteracoes com passo -1")
while contador > 0:
    print(contador, end=" ")
    contador -= 1
print()
    
contador = 10
    
print("5 iteracoes com passo -2")
while contador > 0:
    print(contador, end=" ")
    contador -= 2

