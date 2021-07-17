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
    primo = True
    i = 2

    while i < n // 2 and primo:
        if n % i == 0:
            primo = False
        i = i + 1
    if primo:
        print("Primo")
    else:
        print("Composto")
