#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Entrevista uma quantidade arbitraria de pessoas utilizando
uma unica pergunta e, no final, sumariza as quantidades
de respostas.

@author: Prof. Diogo SM
"""
conta_sim = 0
conta_nao = 0

print("Respostas:")
print("S: sim")
print("N: nao")
print("X: sair")
while True:
    resposta = input("Voce gosta de funk (S|N|X)? ")
    if resposta == "S":
        conta_sim = conta_sim + 1
    elif resposta == "N":
        conta_nao = conta_nao + 1
    elif resposta == "X":
        break
    else:
        print("Resposta invalida")
print("Total sim:", conta_sim)
print("Total nao:", conta_nao)

