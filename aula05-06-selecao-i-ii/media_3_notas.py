#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Calcula a media aritmetica e o status da aprovacao do aluno com base em 
tres notas
@author: Prof. Diogo SM
"""

n1 = float(input("n1: "))
n2 = float(input("n2: "))
n3 = float(input("n3: "))

m = (n1 + n2 + n3) / 3

print(f"Media = {m:.3f}")

if m >= 6.0:
    print("Aprovado")
else:
    print("Reprovado")
