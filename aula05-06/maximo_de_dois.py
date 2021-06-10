#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Determina o máximo de dois números
@author: Prof. Diogo SM
"""

a = int(input("a: "))
b = int(input("b: "))

#if a > b:
#    maximo = a
#else:
#    maximo = b

maximo = a if a > b else b
    
print(f"maximo: {maximo}")
