#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Demonstra efeito colateral da mutacao de uma 
lista em uma funcao.

@author: Prof. Diogo SM
"""

def soma_um(l):
    m = l.copy()
    
    for i in range(len(m)):
        m[i] = m[i] + 1
    
    return m
        

l = [1, 2, 3, 4]

print(l)
print(soma_um(l))
print(l)
    