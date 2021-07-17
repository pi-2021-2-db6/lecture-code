#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Segredo

@author: Prof. Diogo SM
"""

def show(n): # local
    print(n, end=" ")

def subprog():
    n = 12 # local
    
    show(n)
    n = n - 3
    show(n)
    
def impura(x):
    y = x + n
    
    return y
    
n = 10   # global
show(n)
subprog()
show(n)
print()
print(impura(n))