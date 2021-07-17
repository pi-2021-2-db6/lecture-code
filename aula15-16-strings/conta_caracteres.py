#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Funcoes para contagem de caracteres.

@author: Prof. Diogo SM
"""

"""
Testa se um caractere eh uma vogal.
"""
def vogal(c):    
    return len(c) == 1 and c in "aeiouAEIOU"

"""
Testa se um caractere eh uma consoante, assumindo
que o caractere eh alfanumerico ou espaco.
"""
def consoante(c):
    return len(c) == 1 and not vogal(c) and c != " " and not digito(c)

"""
Testa se um caracteres eh um digito.
"""
def digito(c):
    return len(c) == 1 and c in "0123456789"

"""
Informa a quantidade de vogais em uma string.
"""
def conta_vogais(s):
    i = 0
    
    for c in s:
        if vogal(c):
            i += 1
    
    return i

"""
Informa a quantidade de consoantes em uma string.
"""
def conta_consoantes(s):
    i = 0
    
    for c in s:
        if consoante(c):
            i += 1
    
    return i

"""
Informa a quantidade de digitos em uma string.
"""
def conta_digitos(s):
    i = 0
    
    for c in s:
        if digito(c):
            i += 1
    
    return i

"""
Informa a quantidade de espacos na string.
"""
def conta_espacos(s):
    i = 0
    
    for c in s:
        if c == " ":
            i += 1
            
    return i

# Gera uma string contendo apenas as vogais da entrada.
def filtra_vogais(s):
    r = ""
    
    for c in s:
        if vogal(c):
            r = r + c
    
    return r

def filtra_consoantes(s):
    r = ""
    
    for c in s:
        if consoante(c):
            r = r + c
    
    return r

def filtra_alfabetico(s):
    r = ""
    
    for c in s:
        if consoante(c) or vogal(c):
            r = r + c
    
    return r

def teste():
    print(conta_vogais("UFABC 2021"))
    print(conta_vogais("Universidade Federal do ABC 2021"))
    print()
    print(conta_consoantes("UFABC 2021"))
    print(conta_consoantes("Universidade Federal do ABC 2021"))
    print()
    print(conta_digitos("UFABC 2021"))
    print(conta_digitos("Universidade Federal do ABC 2021"))
    
    s = "Universidade Federal do ABC 2021"
    print(conta_vogais(s) + conta_consoantes(s) 
          + conta_digitos(s) + conta_espacos(s) == len(s))
    
    print(filtra_vogais(s))
    print(filtra_consoantes(s))
    print(filtra_alfabetico(s))
    
if __name__ == "__main__":
    teste()