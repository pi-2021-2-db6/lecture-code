#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Calcula o valor de fatorial de x, dado o valor de x.

@author: Prof. Diogo SM
"""
x = int(input("x: "))
f = 1

for i in range(1, x + 1):
    f = f * i
print(f)
