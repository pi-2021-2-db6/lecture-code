#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Demonstra como efetuar somatorios das linhas e 
das colunas de matrizes.

@author: Prof. Diogo SM
"""

import matrizes

def somatorio_linhas(m: [[int]]) -> [int]:
    """
    Calcula os somatorias das linhas de uma matriz.
    - m: a matriz
    - retorna uma lista com os somatorios das respectivas linhas.
    """
    somas = [0] * len(m)
    
    for i in range(len(m)):
        for j in range(len(m[i])):
            somas[i] = somas[i] + m[i][j]
    
    return somas

def somatorio_colunas(m: [[int]]) -> [int]:
    """
    Calcula os somatorias das colunas de uma matriz.
    - m: a matriz
    - retorna uma lista com os somatorios das respectivas colunas.
    """
    if len(m) == 0:
        return []
    
    somas = [0] * len(m[0])
    
    for j in range(len(m[0])):
        for i in range(len(m)):
            somas[j] = somas[j] + m[i][j]
    
    return somas

def testes_linhas():
    v = matrizes.cria_matriz_int_aleatorio(3, 3, 0, 10)
    print(v)
    print(somatorio_linhas(v))
    
    print()
    
    v = matrizes.cria_matriz_int_aleatorio(2, 3, 0, 10)
    print(v)
    print(somatorio_linhas(v))
    
    print()
    
    v = matrizes.cria_matriz_int_aleatorio(1, 1, 0, 10)
    print(v)
    print(somatorio_linhas(v))
    
    print()
    
    v = matrizes.cria_matriz_int_aleatorio(0, 0)
    print(v)
    print(somatorio_linhas(v))

def testes_colunas():
    v = matrizes.cria_matriz_int_aleatorio(3, 3, 0, 10)
    print(v)
    print(somatorio_colunas(v))
    
    print()
    
    v = matrizes.cria_matriz_int_aleatorio(2, 3, 0, 10)
    print(v)
    print(somatorio_colunas(v))
    
    print()
    
    v = matrizes.cria_matriz_int_aleatorio(1, 1, 0, 10)
    print(v)
    print(somatorio_colunas(v))
    
    print()
    
    v = matrizes.cria_matriz_int_aleatorio(0, 0)
    print(v)
    print(somatorio_colunas(v))

def testes():
    #testes_linhas()
    testes_colunas()
    
    
if __name__ == "__main__":
    testes()