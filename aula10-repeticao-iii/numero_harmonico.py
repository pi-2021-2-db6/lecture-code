#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gera o n-esimo numero harmonico, dado o valor de n.

@author: Prof. Diogo SM
"""

n = int(input("n: "))
hn = 0

for i in range(1, n + 1):
    hn = hn + 1 / i
print(f"{hn:.4f}")
