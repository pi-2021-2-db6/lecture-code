#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Demonstra diferentes estrategias para testar se uma 
matriz matematica eh simetrica ou nao.

@author: Prof. Diogo SM
"""
import matriz_transposta

def simetrica(m: [[]]) -> bool:
    """
    Estrategia que envolve a criacao da matriz transposta
    Vantagem: mais simples
    Desvantagem: consome o dobro da memoria
    """
    return m == matriz_transposta.transposta(m)

def simetrica_2(m: [[]]) -> bool:
    """
    Estrategia que envolve o teste das posicoes simetricas.
    Vantagem: economiza memoria
    Desvantagem: menos simples
    """
    if len(m) == 0:
        return True
    l = len(m)
    c = len(m[0])
    
    if l != c:
        return False
    
    for i in range(l):
        for j in range(c):
            if m[i][j] != m[j][i]:
                return False
    
    return True

def teste_simetrica():
    print(simetrica([[1,1], [1,1]]))
    print(simetrica([[1,2], [2,3]]))
    print(simetrica([[1, 7, 3], [7, 4, 5], [3, 5, 6]]))
    print(simetrica([]))
    print(simetrica([[1]]))
    print()
    print(simetrica([[1,1,1], [1,1,1]]))
    print(simetrica([[1,1], [2,1]]))

def teste_simetrica_2():
    print(simetrica_2([[1,1], [1,1]]))
    print(simetrica_2([[1,2], [2,3]]))
    print(simetrica_2([[1, 7, 3], [7, 4, 5], [3, 5, 6]]))
    print(simetrica_2([]))
    print(simetrica_2([[1]]))
    print()
    print(simetrica_2([[1,1,1], [1,1,1]]))
    print(simetrica_2([[1,1], [2,1]]))

def testes():
    teste_simetrica()
    print()
    teste_simetrica_2()
    
if __name__ == "__main__":
    testes()
    
    