#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Testa a primalidade um numero natural maior do que 1.

@author: Prof. Diogo SM
"""

n = int(input("n: "))

if n < 2:
    print("Primalidade indefinida para", n)
elif n == 2:
    print("Primo")
else:
    for i in range(2, n):
        if n % i == 0:
            print("Composto")
            break
    if i == n - 1:
        print("Primo")
