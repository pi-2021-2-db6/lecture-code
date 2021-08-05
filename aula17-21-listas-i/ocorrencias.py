#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Funcoes para contagem e listagem de ocorrencias.

@author: Prof. Diogo SM
"""

def conta_ocorrencias(lista: [], elemento) -> int:
    """
    Informa a quantidade de ocorrencias do elemento 
    na lista.
    - lista: uma lista
    - elemento: o valor a buscar
    - retorna a quantidade de ocorrencias
    """
    contador = 0
    
    for e in lista:
        if e == elemento:
            contador = contador + 1
    
    return contador

def lista_ocorrencias(lista: [], elemento) -> []:
    """
    Gera uma lista contendo todas as posicoes em que o 
    elemento ocorre na lista de entrada
    - lista: a lista de entrada
    - elemento: o valor a buscar
    - retorna uma lista contendo as posicoes das ocorrencias
    """
    res = []
    
    for i in range(len(lista)):
        if lista[i] == elemento:
            res.append(i)
    
    return res

def teste_conta_ocorrencias():
    l = ['a', 'b', 'c', 'a', 'd', 'b', 'e', 'a', 'f', 'g']
    
    print(conta_ocorrencias(l, 'a'))
    print(conta_ocorrencias(l, 'b'))
    print(conta_ocorrencias(l, 'c'))
    print(conta_ocorrencias(l, 'd'))
    print(conta_ocorrencias(l, 'e'))
    print(conta_ocorrencias(l, 'f'))
    print(conta_ocorrencias(l, 'g'))
    
    print(conta_ocorrencias(l, 'h'))
    print(conta_ocorrencias(l, 10))
    print(conta_ocorrencias(l, True))
    
def teste_lista_ocorrencias():
    l = ['a', 'b', 'c', 'a', 'd', 'b', 'e', 'a', 'f', 'g']
    
    print(lista_ocorrencias(l, 'a'))
    print(lista_ocorrencias(l, 'b'))
    print(lista_ocorrencias(l, 'c'))
    print(lista_ocorrencias(l, 'd'))
    print(lista_ocorrencias(l, 'e'))
    print(lista_ocorrencias(l, 'f'))
    print(lista_ocorrencias(l, 'g'))
    
    print(lista_ocorrencias(l, 'h'))
    print(lista_ocorrencias(l, 10))
    print(lista_ocorrencias(l, True))

if __name__ == "__main__":
    teste_conta_ocorrencias()
    print()
    teste_lista_ocorrencias()    
    