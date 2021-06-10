#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Determina o conceito a partir de uma media, bem como
informa se o aluno foi aprovado ou reprovado.

@author: Prof. Diogo SM
"""

media = float(input("Media [0,10]: "))

if 8.5 <= media <= 10.0:
    conceito = "A"
if 7.0 <= media < 8.5:
    conceito = "B"
if 5.5 <= media < 7.0:
    conceito = "C"
if 5.0 <= media < 5.5:
    conceito = "D"
if 0.0 <= media < 5.0:
    conceito = "F"

if conceito == "F":
    print("Reprovado com F")
else:
    print(f"Aprovado com conceito {conceito}")