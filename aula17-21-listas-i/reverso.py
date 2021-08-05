#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Constroi o reverso de uma lista.

@author: Prof. Diogo SM
"""

def reverso(lista: []) -> []:
    """
    Gera reverso usando while
    """
    rev = []
    i = len(lista) - 1
    
    while i >= 0:
        rev.append(lista[i])        
        i = i - 1
        
    return rev

def reverso2(lista: []) -> []:
    """
    Gera reverso usando for..range
    """
    rev = []
    
    for i in range(len(lista) - 1, -1, -1):
        rev.append(lista[i])
        
    return rev

def reverso3(lista: []) -> []:
    """
    Gera reverso usando for..in
    Esta versao consome o dobro de tempo
    das anteriores, pois o metodo insert()
    eh mais ineficiente quando comparado com 
    o metodo append()
    """
    rev = []
    
    for e in lista:
        rev.insert(0, e)
    
    return rev

def teste():
    print(reverso([]))
    print(reverso([1]))
    print(reverso([1, 2]))
    print(reverso([1, 2, 3]))
    print(reverso([1, 2, 3, 4]))
    print()
    print(reverso2([]))
    print(reverso2([1]))
    print(reverso2([1, 2]))
    print(reverso2([1, 2, 3]))
    print(reverso2([1, 2, 3, 4]))
    print()
    print(reverso3([]))
    print(reverso3([1]))
    print(reverso3([1, 2]))
    print(reverso3([1, 2, 3]))
    print(reverso3([1, 2, 3, 4]))
    
if __name__ == "__main__":
    teste()
    