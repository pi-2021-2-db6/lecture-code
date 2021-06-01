#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exemplo de como ler 3 inteiros na mesma linha, separados
por espaço.

Como usar: rodar o programa e digitar uma lista de 3 inteiros,
por exemplo 39 92 19
O que acontece: o programa irá extrair os inteiros e mostrá-los
um por linha, e depois a soma, para demonstrar que conseguiu obter os números
separadamente

Você pode adaptar essa estratégia para 2, 4, 5,... inteiros e 
assim por diante, basta mudar a quantidade de variáveis
@author: Prof. Diogo SM
"""

# "Corta" a string de entrada sempre que encontrar um espaço, 
# por exemplo, "39 92 19" vira três strings, "39", "92", "19", 
# que são armazenadas, respectivamente, em a, b, c
a, b, c = input().split(" ")

# como a, b, c, são strings, preciso convertê-las para inteiro
# obs: se a entrada fosse de reais, converteríamos para float, 
# e assim por diante
a1 = int(a)
b1 = int(b)
c1 = int(c)

# Agora vou exibir os valores um por linha e no final sua soma, 
# para demonstrar que de fato extraí os valores e que de fato
# são números
print(a1)
print(b1)
print(c1)
print(a1 + b1 + c1)

