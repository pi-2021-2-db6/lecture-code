#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lista todos os divisores de n.

@author: Prof. Diogo SM
"""

n = int(input("n: "))

if n > 1:
    print(1, end=" ")
for k in range(2, n // 2 + 1):
    if n % k == 0:
        print(k, end=" ")
print(n)