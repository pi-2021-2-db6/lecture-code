#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Determina o conceito a partir de uma media, bem como
informa se o aluno foi aprovado ou reprovado.

@author: Prof. Diogo SM
"""

media = float(input("Media [0,10]: "))

if media <= 10.0:
    conceito = "A"
elif media < 8.5:
    conceito = "B"
elif media < 7.0:
    conceito = "C"
elif media < 5.5:
    conceito = "D"
elif 0.0 <= media < 5.0:
    conceito = "F"
else:
    conceito = "invalido"

if conceito == "F":
    print("Reprovado com F")
elif conceito == "invalido":
    print("Media invalida")
else:
    print(f"Aprovado com conceito {conceito}")