#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bibliotecas de funcoes que efetuam operacoes aritmeticas
sobre matrizes.

@author: Prof. Diogo SM
"""

import matrizes

def soma_matrizes(a: [[int]], b: [[int]]) -> [[int]]:
    """
    Calcula a soma entre duas matrizes.
    """
    if len(a) != len(b):
        raise Exception("Matrizes com qtde. divergentes de linhas ")
    if len(a) == 0:
        return []
    if len(a[0]) != len(b[0]):
        raise Exception("Matrizes com qtde. divergentes de colunas")
    
    l = len(a)
    c = len(a[0])
    res = matrizes.cria_matriz_zeros(l, c)
    for i in range(l):
        for j in range(c):
            res[i][j] = a[i][j] + b[i][j]
            
    return res

def diferenca_matrizes(a: [[int]], b: [[int]]) -> [[int]]:
    """
    Calcula a diferenca entre duas matrizes.
    """
    if len(a) != len(b):
        raise Exception("Matrizes com qtde. divergentes de linhas ")
    if len(a) == 0:
        return []
    if len(a[0]) != len(b[0]):
        raise Exception("Matrizes com qtde. divergentes de colunas")
    
    l = len(a)
    c = len(a[0])
    res = matrizes.cria_matriz_zeros(l, c)
    for i in range(l):
        for j in range(c):
            res[i][j] = a[i][j] - b[i][j]
            
    return res
            
def testes_soma():
    a = matrizes.cria_matriz_int_aleatorio(3, 3, 0, 10)
    print(matrizes.formata_matriz_int(a, 5))
    b = matrizes.cria_matriz_int_aleatorio(3, 3, 0, 10)
    print(matrizes.formata_matriz_int(b, 5))
    c = soma_matrizes(a, b)
    print(matrizes.formata_matriz_int(c, 5))
    
    print()
    
    a = matrizes.cria_matriz_int_aleatorio(3, 2, 0, 10)
    print(matrizes.formata_matriz_int(a, 5))
    b = matrizes.cria_matriz_int_aleatorio(3, 2, 0, 10)
    print(matrizes.formata_matriz_int(b, 5))
    c = soma_matrizes(a, b)
    print(matrizes.formata_matriz_int(c, 5))
    
    print()
    
    a = matrizes.cria_matriz_int_aleatorio(2, 3, 0, 10)
    print(matrizes.formata_matriz_int(a, 5))
    b = matrizes.cria_matriz_int_aleatorio(2, 3, 0, 10)
    print(matrizes.formata_matriz_int(b, 5))
    c = soma_matrizes(a, b)
    print(matrizes.formata_matriz_int(c, 5))
    
    print()
    
    a = matrizes.cria_matriz_int_aleatorio(0, 0, 0, 10)
    print(matrizes.formata_matriz_int(a, 5))
    b = matrizes.cria_matriz_int_aleatorio(0, 0, 0, 10)
    print(matrizes.formata_matriz_int(b, 5))
    c = soma_matrizes(a, b)
    print(matrizes.formata_matriz_int(c, 5))
    
    print()
    
    #a = matrizes.cria_matriz_int_aleatorio(2, 3, 0, 10)
    #print(matrizes.formata_matriz_int(a, 5))
    #b = matrizes.cria_matriz_int_aleatorio(3, 3, 0, 10)
    #print(matrizes.formata_matriz_int(b, 5))
    #c = soma_matrizes(a, b)
    #print(matrizes.formata_matriz_int(c, 5))
    
    #print()
    
    a = matrizes.cria_matriz_int_aleatorio(2, 2, 0, 10)
    print(matrizes.formata_matriz_int(a, 5))
    b = matrizes.cria_matriz_int_aleatorio(2, 3, 0, 10)
    print(matrizes.formata_matriz_int(b, 5))
    c = soma_matrizes(a, b)
    print(matrizes.formata_matriz_int(c, 5))
    
def testes_diferenca():
    a = matrizes.cria_matriz_int_aleatorio(3, 3, 0, 10)
    print(matrizes.formata_matriz_int(a, 5))
    b = matrizes.cria_matriz_int_aleatorio(3, 3, 0, 10)
    print(matrizes.formata_matriz_int(b, 5))
    c = diferenca_matrizes(a, b)
    print(matrizes.formata_matriz_int(c, 5))
    
    print()
    
    a = matrizes.cria_matriz_int_aleatorio(3, 2, 0, 10)
    print(matrizes.formata_matriz_int(a, 5))
    b = matrizes.cria_matriz_int_aleatorio(3, 2, 0, 10)
    print(matrizes.formata_matriz_int(b, 5))
    c = diferenca_matrizes(a, b)
    print(matrizes.formata_matriz_int(c, 5))
    
    print()
    
    a = matrizes.cria_matriz_int_aleatorio(2, 3, 0, 10)
    print(matrizes.formata_matriz_int(a, 5))
    b = matrizes.cria_matriz_int_aleatorio(2, 3, 0, 10)
    print(matrizes.formata_matriz_int(b, 5))
    c = diferenca_matrizes(a, b)
    print(matrizes.formata_matriz_int(c, 5))
    
    print()
    
    a = matrizes.cria_matriz_int_aleatorio(0, 0, 0, 10)
    print(matrizes.formata_matriz_int(a, 5))
    b = matrizes.cria_matriz_int_aleatorio(0, 0, 0, 10)
    print(matrizes.formata_matriz_int(b, 5))
    c = diferenca_matrizes(a, b)
    print(matrizes.formata_matriz_int(c, 5))
    
    print()
    
    # a = matrizes.cria_matriz_int_aleatorio(2, 3, 0, 10)
    # print(matrizes.formata_matriz_int(a, 5))
    # b = matrizes.cria_matriz_int_aleatorio(3, 3, 0, 10)
    # print(matrizes.formata_matriz_int(b, 5))
    # c = diferenca_matrizes(a, b)
    # print(matrizes.formata_matriz_int(c, 5))
    
    # print()
    
    # a = matrizes.cria_matriz_int_aleatorio(2, 2, 0, 10)
    # print(matrizes.formata_matriz_int(a, 5))
    # b = matrizes.cria_matriz_int_aleatorio(2, 3, 0, 10)
    # print(matrizes.formata_matriz_int(b, 5))
    # c = diferenca_matrizes(a, b)
    # print(matrizes.formata_matriz_int(c, 5))
    
def testes():
    # testes_soma()
    testes_diferenca()
    
if __name__ == "__main__":
    testes()
    