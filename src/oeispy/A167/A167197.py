# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A167197

from math import gcd
def aupton(nn):
    alst = [7]
    for n in range(7, nn+1): alst.append(alst[-1] + gcd(n, alst[-1]))
    return alst
print(aupton(68)) # _Michael S. Branicky_, Jul 14 2021

