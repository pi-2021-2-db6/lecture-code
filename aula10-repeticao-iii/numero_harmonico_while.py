#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gera o n-esimo numero harmonico, dado o valor de n.

@author: Prof. Diogo SM
"""

n = int(input("n: "))
hn = 0
i = 1

while i <= n:
    hn = hn + 1 / i
    i = i + 1
print(f"{hn:.4f}")
