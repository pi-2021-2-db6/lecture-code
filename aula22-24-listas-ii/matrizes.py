#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Biblioteca de funcoes utilitarias para processamento
de matrizes.

@author: Prof. Diogo SM
"""

import random

def cria_matriz_zeros(l: int, c: int) -> [[float]]:
    """
    Cria uma matriz real de zeros.
    - l: qtde. de linhas
    - c: qtde. de colunas
    """
    v = []
    
    for i in range(l):
        v.append([])
        for j in range(c):
            v[i].append(0.0)
        
    return v

def cria_matriz_zeros_int(l: int, c: int) -> [[int]]:
    """
    Cria uma matriz int de zeros.
    - l: qtde. de linhas
    - c: qtde. de colunas
    """
    v = []
    
    for i in range(l):
        v.append([])
        for j in range(c):
            v[i].append(0)
        
    return v

def cria_matriz_int_aleatorio(l: int, c: int, 
                              li: int = 0, 
                              ls: int = 100) -> [[int]]:
    """
    Cria uma matriz de inteiros aleatorios.
    - l: qtde. de linhas
    - c: qtde. de colunas
    - li: limite inferior para os numeros aleatorios
    - ls: limite superior para os numeros aleatorios
    """
    v = []
    
    for i in range(l):
        v.append([])
        for j in range(c):
            v[i].append(random.randint(li, ls))
        
    return v

def cria_matriz_float_aleatorio(l: int, c: int, 
                                li: int = 0.0, 
                                ls: int = 100.0) -> [[float]]:
    """
    Cria uma matriz de floats aleatorios.
    - l: qtde. de linhas
    - c: qtde. de colunas
    - li: limite inferior para os numeros aleatorios
    - ls: limite superior para os numeros aleatorios
    """
    v = []
    
    for i in range(l):
        v.append([])
        for j in range(c):
            v[i].append(random.uniform(li, ls))
        
    return v

def formata_matriz_int(m: [[int]], l: int) -> str:
    """
    Gera uma string com a matriz no formato retangular.
    - m: a matriz de int
    - l: a largura da coluna
    """
    s = ""
    
    for i in range(len(m)):
        for j in range(len(m[i])):
            s = s + f"{m[i][j]:{l}}"
        s = s + "\n"
        
    return s

def formata_matriz_float(m: [[float]], l: int) -> str:
    """
    Gera uma string com a matriz no formato retangular.
    - m: a matriz de float
    - l: a largura da coluna
    """
    s = ""
    
    for i in range(len(m)):
        for j in range(len(m[i])):
            s = s + f"{m[i][j]:{l}.3f}"
        s = s + "\n"
        
    return s

def testes():
    # print(cria_matriz_int_aleatorio(2, 3, 90))
    # print(cria_matriz_int_aleatorio(3, 3, 5, 10))
    # print(cria_matriz_int_aleatorio(0, 0))
    #print(cria_matriz_zeros(3, 3))
    #print(cria_matriz_zeros(2, 4))
    #print(cria_matriz_zeros(1, 1))
    #print(cria_matriz_zeros(0, 0))
    m_a = cria_matriz_int_aleatorio(2, 3)
    m_b1 = m_a
    m_b2 = cria_matriz_int_aleatorio(2, 3)
    
    print(m_a)
    print(m_b1)
    print(m_b2)
    
if __name__ == "__main__":
    testes()