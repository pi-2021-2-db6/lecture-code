#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dadas as coordenadas de um ponto e as caracteristicas de uma circunferencia,
determina se o ponto esta dentro ou fora da circunferencia

@author: Prof. Diogo SM
"""

import math

c = float(input("Coordenada x do centro da circunferencia: "))
d = float(input("Coordenada y do centro da circunferencia: "))
r = float(input("Raio da circunferencia: "))
p = float(input("Coordenada x do ponto: "))
q = float(input("Coordenada y do ponto: "))

distancia = math.sqrt((p - c) * (p - c) + (q - d) * (q - d))

if distancia > r:
    print("Fora")
else:
    print("Dentro")

