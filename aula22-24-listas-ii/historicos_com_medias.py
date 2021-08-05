#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercicio que envolve a construcao de uma matriz aumentada
com as medias dos historicos.

@author: Prof. Diogo SM
"""

import matrizes

def calcula_medias(historicos: [[float]]) -> [[float]]:
    """
    Aumenta a matriz de historicos com as medias (coluna adicional)
    - a matriz de historicos
    - retorna a matriz aumentada com a medias
    """
    if len(historicos) == 0:
        return []
    
    l = len(historicos)
    c = len(historicos[0])
    res = matrizes.cria_matriz_zeros(l, c + 1)
    
    for i in range(l):
        for j in range(c):
            res[i][j] = historicos[i][j]
            res[i][c] = res[i][c] + historicos[i][j]
        res[i][c] = res[i][c] / c
        
    return res

def testes():
    v = matrizes.cria_matriz_float_aleatorio(3, 2, 0, 10)
    print(matrizes.formata_matriz_float(v, 6))
    print(matrizes.formata_matriz_float(calcula_medias(v), 6))
    
    print()
    
    v = matrizes.cria_matriz_float_aleatorio(20, 5, 0, 10)
    print(matrizes.formata_matriz_float(v, 6))
    print(matrizes.formata_matriz_float(calcula_medias(v), 6))

if __name__ == "__main__":
    testes()