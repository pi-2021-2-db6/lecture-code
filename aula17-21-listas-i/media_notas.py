#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Calcula a media de n notas, sendo n um valor definido pelo
usuario.

@author: Prof. Diogo SM
"""

def calcula_media(qtde_notas: int) -> float:
    """
    Funcao impura que calcula a media de uma 
    quantidade de notas
    - qtde_notas: inteiro
    - retorna um float contendo a media
    """
    soma = 0.0
    
    for i in range(qtde_notas):
        nota = float(input())
        soma += nota
    
    if qtde_notas > 0:
        media = soma / qtde_notas
    else:
        media = 0.0
        
    return media

def testes():    
    print(f"{calcula_media(3):.3f}")

if __name__ == "__main__":
    testes()