# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A051024

from sympy import nextprime; a, p = 0, 2
for n in range(2, 50917):
    p=nextprime(p); a += p%4-2
    if a == -1: print(n, end = ', ') # _Ya-Ping Lu_, Jan 18 2025

