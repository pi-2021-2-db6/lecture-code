#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Calcula a media aritmetica de uma quantidade arbitraria de notas.

@author: Prof. Diogo SM
"""

soma = 0.0
qtde_notas = 0

while True:
    nota = float(input("Nota: "))
    if nota < 0:
        break
    soma = soma + nota
    qtde_notas = qtde_notas + 1
if qtde_notas > 0:
    media = soma / qtde_notas
    print(f"Media = {media:.3f}")