#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Demonstra as diferentes tecnicas classicas para percorrer
(visitar todos os elementos) de uma matriz.

@author: Prof. Diogo SM
"""

import matrizes

def percorre_por_linhas(m: [[]]):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(f"m[{i}][{j}] =", m[i][j])

def percorre_por_colunas(m: [[]]):
    if len(m) > 0:
        for j in range(len(m[0])):
            for i in range(len(m)):
                print(f"m[{i}][{j}] =", m[i][j])
            
def testes():
    v = matrizes.cria_matriz_int_aleatorio(3, 4)
    print(v)
    percorre_por_linhas(v)
    percorre_por_linhas([])
    
    print()
    
    percorre_por_colunas(v)
    percorre_por_colunas([])
    
if __name__ == "__main__":
    testes()