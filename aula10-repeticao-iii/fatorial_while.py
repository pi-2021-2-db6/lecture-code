#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Calcula o valor de fatorial de x, dado o valor de x.

@author: Prof. Diogo SM
"""
x = int(input("x: "))
f = 1
i = 1

while i <= x:
    f = f * i
    i = i + 1
print(f)
