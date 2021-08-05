#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Calcula o produto escalar entre dois vetores

@author: Prof. Diogo SM
"""

def produto_escalar(p: [float], q: [float]) -> float:
    if len(p) != len(q):
        raise Exception("Os vetores tem tamanhos diferentes")
    
    res = 0.0
    
    for i in range(len(p)):
        res = res + p[i] * q[i]
        
    return res

def teste():
    print(produto_escalar([], []))
    print(produto_escalar([2], [2]))
    print(produto_escalar([1, 2], [3, 4]))
    print(produto_escalar([1, 2, 3], [3, 4, 5]))
    
if __name__ == "__main__":
    teste()