#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Define e testa a funcao que gera o n-esimo numero
harmonico, dado o valor de n.

@author: Prof. Diogo SM
"""

def harmonico(n):
    h = 0.0
    
    for i in range(1, n + 1):
        h = h + 1.0 / i
    
    return h

# codigo global
print(harmonico(1))
print(harmonico(2))
print(harmonico(12))