#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercicio que envolve a criacao de uma matriz aumentada
com os somatorios de suas linhas e suas colunas.

@author: Prof. Diogo SM
"""
import matrizes

def cria_matriz_aumentada(m: [[int]]) -> [[int]]:
    """
    Gera uma matriz aumentada com os somatorios das linhas
    e das colunas.
    - m: a matriz original
    - retorna a matriz aumentada
    """
    if len(m) == 0:
        return m
    
    l = len(m)
    c = len(m[0])
    res = matrizes.cria_matriz_zeros_int(l + 1, c + 1)
    
    for i in range(l):
        for j in range(c):
            res[i][j] = m[i][j]
            res[i][c] = res[i][c] + m[i][j]
            res[l][j] = res[l][j] + m[i][j]            
            res[l][c] = res[l][c] + m[i][j]        
            
    return res

def testes():
    m = matrizes.cria_matriz_int_aleatorio(3, 3, 0, 10)
    print(m)
    print(cria_matriz_aumentada(m))
    
    
if __name__ == "__main__":
    testes()
    