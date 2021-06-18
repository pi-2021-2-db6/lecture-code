#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Calcula a media aritmetica de 10 notas.
(utiliza estrutura while)

@author: Prof. Diogo SM
"""
contador = 0
soma = 0.0

while contador < 10:
    nota = float(input("Nota: "))
    soma = soma + nota
    contador = contador + 1
media = soma / 10
print(f"Media = {media:.3f}")
