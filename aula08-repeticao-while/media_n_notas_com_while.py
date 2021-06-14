#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Calcula a media aritmetica de n notas.
(utiliza estrutura while)

@author: Prof. Diogo SM
"""
contador = 0
soma = 0.0
n = 0

while n <= 0:
    n = int(input("Qtde de notas: "))
while contador < n:
    nota = float(input("Nota: "))
    soma = soma + nota
    contador = contador + 1

media = soma / n
print(f"Media = {media:.3f}")
