#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Classifica o triangulo de acordo com o numero de lados

@author: Prof. Diogo SM
"""
a = float(input("Lado A: "))
b = float(input("Lado B: "))
c = float(input("Lado C: "))

if a + b > c and b + c > a and c + a > b:
    if a == b == c:
        print("Equilatero")
    elif a != b and a != c and b != c:
        print("Escaleno")
    else:
        print("Isosceles")
else:
    print("Nao eh triangulo")
