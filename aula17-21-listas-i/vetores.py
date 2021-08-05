#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Biblioteca de operacoes aritmeticas sobre vetores
matematicos.

@author: Prof. Diogo SM
"""

def produto_escalar(p: [float], q: [float]) -> float:
    """
    Produto escalar entre dois vetores float
    """
    if len(p) != len(q):
        raise Exception("Os vetores tem tamanhos diferentes")
    
    res = 0.0
    
    for i in range(len(p)):
        res = res + p[i] * q[i]
        
    return res

def adiciona(p: [float], q: [float]) -> [float]:
    """
    Adicao entre dois vetores
    """
    if len(p) != len(q):
        raise Exception("Os vetores tem tamanhos diferentes")
    
    res = []
    
    for i in range(len(p)):
        res.append(p[i] + q[i])
        
    return res

def subtrai(p: [float], q: [float]) -> [float]:
    """
    Subtracao entre dois vetores
    """
    if len(p) != len(q):
        raise Exception("Os vetores tem tamanhos diferentes")
    
    res = []
    
    for i in range(len(p)):
        res.append(p[i] - q[i])
        
    return res

def multiplica_escalar(c: float, p: [float]) -> [float]:
    """
    Multiplicacao de um escalar por um vetor.
    """
    res = []
    
    for pi in p:
        res.append(c * pi)
        
    return res

def teste_multiplica_escalar():
    print(multiplica_escalar(3, []))
    print(multiplica_escalar(3, [2]))
    print(multiplica_escalar(3, [2, 4]))
    print(multiplica_escalar(3, [2, 4, 9]))

def teste_produto_escalar():
    print(produto_escalar([], []))
    print(produto_escalar([2], [2]))
    print(produto_escalar([1, 2], [3, 4]))
    print(produto_escalar([1, 2, 3], [3, 4, 5]))
    
def teste_adiciona():
    print(adiciona([], []))
    print(adiciona([1], [4]))
    print(adiciona([1, 2], [4, 5]))
    print(adiciona([1, 2, 3], [4, 5, 6]))
    #print(adiciona([1], [2, 3]))

def teste_subtrai():
    print(subtrai([], []))
    print(subtrai([1], [4]))
    print(subtrai([1, 2], [4, 5]))
    print(subtrai([1, 2, 3], [4, 5, 6]))
    #print(subtrai([1], [2, 3]))
    
    
if __name__ == "__main__":
    teste_multiplica_escalar()