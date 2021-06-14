#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exibe os dois valores digitados em ordem crescente
@author: Prof. Diogo SM
"""

x = int(input("x = "))
y = int(input("y = "))

if x > y:
    temp = x
    x = y
    y = temp
print(f"x = {x}")
print(f"y = {y}")