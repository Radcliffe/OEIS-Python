# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A339085

from sympy import primepi
for n in range(1, 101):
    m = primepi(n)
    print (primepi(n + m) - primepi(n - m))

