# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A266388

from sympy import isprime
def afind(limit, startk=0):
    pow2 = 2**startk
    for k in range(startk, limit+1):
        if isprime(int(str(pow2) + str(pow2 - 1))): print(k, end=", ")
        pow2 *= 2
afind(600) # _Michael S. Branicky_, Sep 08 2021

