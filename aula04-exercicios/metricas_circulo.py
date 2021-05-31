#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Calcula o diametro, o perimetro e a area do circulo, dado o raio
@author: Prof. Diogo SM
"""
import math

r = float(input("Raio: "))

d = r + r
p = 2 * math.pi * r
a = math.pi * r * r

print(f"Diametro: {d:.3f}")
print(f"Perimetro: {p:.3f}")
print(f"Area: {a:.3f}")

