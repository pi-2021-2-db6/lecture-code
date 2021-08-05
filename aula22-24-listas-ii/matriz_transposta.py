#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Algoritmo para transposicao de matrizes.

@author: Prof. Diogo SM
"""

import matrizes

def transposta(m: [[int]]) -> [[int]]:
    """
    Gera a transposta da matriz.
    - m: a matriz
    - retorna a transposta de m
    """
    l = len(m)
    
    if l == 0:
        return []
    
    c = len(m[0])
    mt = matrizes.cria_matriz_zeros_int(c, l)
    
    for i in range(l):
        for j in range(c):
            mt[j][i] = m[i][j]
    
    return mt

def testes():
    m1 = matrizes.cria_matriz_int_aleatorio(3, 3)
    print(matrizes.formata_matriz_int(m1, 4))
    m1t = transposta(m1)
    print(matrizes.formata_matriz_int(m1t, 4))
    
    print()
    
    m1 = matrizes.cria_matriz_int_aleatorio(5, 3)
    print(matrizes.formata_matriz_int(m1, 4))
    m1t = transposta(m1)
    print(matrizes.formata_matriz_int(m1t, 4))
    
    print()
    
    m1 = matrizes.cria_matriz_int_aleatorio(0, 0)
    print(m1)
    m1t = transposta(m1)
    print(m1t)
    
    print()
    
    m1 = matrizes.cria_matriz_int_aleatorio(1, 1)
    print(matrizes.formata_matriz_int(m1, 4))
    m1t = transposta(m1)
    print(matrizes.formata_matriz_int(m1t, 4))
    
if __name__ == "__main__":
    testes()
    
    