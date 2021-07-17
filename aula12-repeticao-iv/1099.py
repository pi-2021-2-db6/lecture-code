#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Solucao para o URI 1099 
(Soma de impares consecutivos ii)

@author: Prof. Diogo SM
"""

n = int(input())

for i in range(n):
    x_str, y_str = input().split()
    x_int, y_int = int(x_str), int(y_str)
    x = min(x_int, y_int)
    y = max(x_int, y_int)
    s = 0
    
    for j in range(x + 1, y):
        if j % 2 != 0:
            s = s + j
    print(s)
    