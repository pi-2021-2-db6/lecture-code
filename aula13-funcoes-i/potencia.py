#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Efetua a operacao de potenciacao, considerando
expoente positivo.

@author: Prof. Diogo SM
"""

def potencia(b, e):
    p = 1
    
    for i in range(e):
        p = p * b
        
    return p

a = potencia(2, 3)
b = potencia(4, a)
c = potencia(4, potencia(potencia(2,1), 3))

print(f"2**3 = {a}")
print(f"4**{a} = {b}")
print(f"4**{a} = {c}")
