# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A280870

from math import gcd
from sympy import nextprime
def aupton(terms):
    alst, p, q, r, s = [], 2, 3, 5, 7
    while len(alst) < terms:
        alst.append((p+r)//gcd(p+r, q+s))
        p, q, r, s = q, r, s, nextprime(s)
    return alst
print(aupton(61)) # _Michael S. Branicky_, Oct 08 2021

