# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A275767

from sympy import isprime
def afind(limit, startk=2):
    alst, pow4 = [], 4**startk
    for k in range(startk, limit+1):
        if isprime(2*pow4 - 27): print(k, end=", ")
        pow4 *= 4
afind(1300) # _Michael S. Branicky_, Sep 22 2021

