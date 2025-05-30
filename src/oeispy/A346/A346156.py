# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A346156

from sympy import isprime
def aupto(lim):
    xkx = set(x**k + x + 1 for k in range(2, lim.bit_length()) for x in range(int(lim**(1/k))+2))
    return sorted(filter(isprime, filter(lambda t: t<=lim, xkx)))
print(aupto(14000)) # _Michael S. Branicky_, Jul 07 2021

