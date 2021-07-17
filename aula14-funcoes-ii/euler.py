#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Aproxima o numero de euler utilizando uma serie
finita com k termos.

@author: Prof. Diogo SM
"""

def fatorial(x):
    f = 1
    
    for i in range(1, x + 1):
        f = f * i
    
    return f

def testa_fatorial(k):
    for i in range(k):
        print(i, "\t", fatorial(i))
        
def euler(k):
    e = 0.0
    
    for n in range(0, k + 1):
        e = e + 1 / fatorial(n)
    
    return e

def main():
    print("Eu sou o codigo global da euler")
    print("Eu executei!")
    
if __name__ == "__main__":
    main()
