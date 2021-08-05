#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Diferentes metodos para percorrer uma lista

@author: Prof. Diogo SM
"""

l = ["one", "two", "three", "four", "five"]

# com while
i = 0

while i < len(l):
    print(l[i])
    i += 1
    
print()

# com for...range
for i in range(len(l)):
    print(l[i])
    
print()
    
# com for...in
for e in l:
    print(e)
