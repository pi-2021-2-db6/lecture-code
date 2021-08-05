#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Retorna o indice da primeira ocorrencia do
    elemento na lista.
    - l: a lista onde sera feita a busca
    - e: o elemento a buscar na lista
    - retorna: a posicao da primeira ocorrencia
@author: Prof. Diogo SM
"""

def indice(l: [], e) -> int:
    for i in range(len(l)):
        if e == l[i]:
            return i
    raise Exception("O elemento nao esta na lista")
    
def teste():
    l = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    
    print(indice(l, 'a'))
    print(indice(l, 'b'))
    print(indice(l, 'c'))
    print(indice(l, 'd'))
    print(indice(l, 'e'))
    print(indice(l, 'f'))
    print(indice(l, 'g'))
    print(indice(l, 'h'))
    
if __name__ == "__main__":
    teste()