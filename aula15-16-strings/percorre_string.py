#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Varios modos de percorrer uma string.

@author: Prof. Diogo SM
"""

s = input()

# usando for..in com contador
for i in range(len(s)):
    print(s[i])
    
print()
    
# usando while
i = 0

while i < len(s):
    print(s[i])
    i += 1
    
print()

# usando for..in sem contador
for c in s:
    print(c)

