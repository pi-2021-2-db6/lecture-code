#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Calcula o perimetro, a area e a diagonal do retangulo, dadas a base e a altura
@author: Prof. Diogo SM
"""
import math

b = float(input("Base: "))
h = float(input("Altura: "))

p = 2 * b + 2 * h
a = b * h
d = math.sqrt(b*b + h*h)

print(f"Perimetro: {p:.3f}")
print(f"Area: {a:.3f}")
print(f"Diagonal: {d:.3f}")

# Exercicio: faça um outro programa análogo, porém, para quadrados


