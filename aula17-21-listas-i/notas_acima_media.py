#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Le um quantidade fixa de notas e informa quantas estao 
acima da media.

@author: Prof. Diogo SM
"""

def le_notas(qtde: int) -> [float]:
    """
    Le a partir do teclado uma quantidade fixa de notas.
    - qtde: a quantidade de notas
    - retorna uma lista de notas (float)
    """
    notas = []
    
    for i in range(qtde):
        notas.append(float(input()))
    
    return notas

def calcula_media(notas: [float]) -> float:
    """
    Calcula a media de uma lista de notas.
    - notas: lista de notas (float)
    - retorna a media das notas (float)
    """
    return sum(notas) / len(notas) if len(notas) > 0 else 0.0

def qtde_acima_media(notas: [float], media: float) -> int:
    """
    Informa a quantidade de notas cujos valores estao 
    acima da media.
    - notas: a lista de notas
    - media: a media
    - retorna a quantidade de notas acima da media
    """
    c = 0
    
    for nota in notas:
        if nota > media:
            c += 1
    
    return c

def acima_media(notas: [float], media: float) -> [float]:
    """
    Filtra as notas que estao acima da media
    - notas: a lista de notas
    - media: a media das notas
    - retorna uma lista das notas que estao acima da media
    """
    res = []
    
    for nota in notas:
        if nota > media:
            res.append(nota)
    
    return res

def testes():
    #v = le_notas(4)
    #print(v)
    #print(calcula_media(v))
    
    print(calcula_media([]))
    
    n = [1, 2, 3, 4]
    m = calcula_media(n)
    
    print(n)
    print(m)
    print(acima_media(n, m))
    
def main():
    """
    Programa principal
    """
    qtde = int(input("Quantidade de notas: "))
    
    notas = le_notas(qtde)   
    media = calcula_media(notas)
    notas_acima_media = acima_media(notas, media)
    
    print(f"Media: {media:.3f}")
    print(f"Temos {len(notas_acima_media)} nota(s) acima da media: {notas_acima_media}")
    
if __name__ == "__main__":
    #testes()
    main()