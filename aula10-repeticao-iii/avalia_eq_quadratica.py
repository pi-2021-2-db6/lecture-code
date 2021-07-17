#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Avalia a equacao y = 2*x**2 + 3*x - 5 para valores de 
x variando no intervalo [0,n], sendo que n eh uma
entrada do programa.

@author: Prof. Diogo SM
"""

n = int(input("n: "))

print("y = 2 * x ** 2 + 3 * x - 5")
print(f"{'x':^7} {'y':^7}")
for x in range(0, n + 1):
    y = 2 * x ** 2 + 3 * x - 5
    print(f"{x:^7} {y:^7}")
