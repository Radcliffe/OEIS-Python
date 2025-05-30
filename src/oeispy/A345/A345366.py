# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A345366

from sympy import nextprime
def aupton(nn):
    alst, p, q = [], 2, 3
    while len(alst) < nn: alst.append((p*q+1)%(p+q)); p, q = q, nextprime(q)
    return alst
print(aupton(62)) # _Michael S. Branicky_, Jun 16 2021

