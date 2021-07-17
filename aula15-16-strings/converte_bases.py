#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Converte entre diferentes bases numericas.

@author: Prof. Diogo SM
"""

import math

"""
Converte um inteiro positivo na base 10 para a 
representacao em string do numero na base 2
"""
def dec_bin(n):
    if n == 0:
        return "0"
        
    b = ""
    
    while n > 0:
        b = str(n % 2) + b
        n = n // 2
    
    return b

"""
Converte a string com a representacao binaria para o 
equivalente inteiro positivo
"""
def bin_dec(b):
    n = 0
    
    for i in range(len(b)):
        d = int(b[i])
        n = n + d * int(math.pow(2, len(b) - 1 - i))
    
    return n
    

def testes():
    print(dec_bin(0))
    print(dec_bin(1))
    print(dec_bin(10))
    print(dec_bin(15))
    print(dec_bin(100))
    print(dec_bin(101))
    print(dec_bin(4611686018427387904))
    print()
    print(bin_dec("1010"))
    print(bin_dec("1100100"))
    print(bin_dec("1100101"))
    print(bin_dec("0"))
    print(bin_dec("1111"))
    print(bin_dec("100000000000000000000000000000000000000000000000000000000000000"))
    
if __name__ == "__main__":
    testes()