# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A337788

from sympy import primepi
for n in range(1, 101):
    pi = primepi(n)
    a = primepi(n + pi) - pi
    print(a)

