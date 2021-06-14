#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Determina quantas raizes (e qual tipo) tem a equacao quadratica, 
dados os coeficientes
@author: Prof. Diogo SM
"""

print("Considere a * x * x + b * x + c")
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

if a == 0:
    print("Nao eh equacao quadratica")
else:
    d = b * b - 4 * a * c
    if d > 0:
        print("Duas raizes reais distintas")
    else:
        if d < 0:
            print("Raizes complexas")
        else:
            print("Uma raiz real")
    if a > 0:
        print("Concavidade para cima")
    else:
        print("Concavidade para baixo")
    
