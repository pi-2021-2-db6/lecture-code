#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
URI 1221: Primo rapido

@author: Prof. Diogo SM
"""
import math

n = int(input())

for i in range(n):
    x = int(input())
    if x == 1:
        print("Not Prime")
    elif x == 2:
        print("Prime")
    else:
        prime = True
        k = 2
        
        while k <= math.sqrt(x) and prime:
            if x % k == 0:
                prime = False
            k = k + 1
        if prime:
            print("Prime")
        else:
            print("Not Prime")
