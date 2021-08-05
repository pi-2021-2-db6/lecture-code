#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Cria um historico estatico das notas de 5 alunos
em 5 disciplinas.

Demonstra como acessar os elementos de uma matriz.

@author: Prof. Diogo SM
"""

historicos = [[0.0] * 5, 
              [0.0] * 5,
              [0.0] * 5,
              [0.0] * 5,
              [0.0] * 5]


historicos[0][0] = 5.5
historicos[0][1] = 8.3
historicos[0][2] = 6.5
historicos[0][3] = 10.0
historicos[0][4] = 9.5

historicos[1][0] = 8.0
historicos[1][1] = 7.5
historicos[1][2] = 8.5
historicos[1][3] = 6.5
historicos[1][4] = 10.0

historicos[2][0] = 7.5
historicos[2][1] = 8.0
historicos[2][2] = 9.0
historicos[2][3] = 8.0
historicos[2][4] = 8.5

historicos[3][0] = 6.5
historicos[3][1] = 3.5
historicos[3][2] = 6.5
historicos[3][3] = 4.5
historicos[3][4] = 9.0

historicos[4][0] = 8.0
historicos[4][1] = 9.5
historicos[4][2] = 8.0
historicos[4][3] = 10.0
historicos[4][4] = 9.0

print(historicos)

for i in range(len(historicos)):
    print(historicos[i])


