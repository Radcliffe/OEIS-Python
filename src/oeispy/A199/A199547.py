# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A199547

from sympy import nextprime; a, p = 0, 2
while p < 617717:
    p=nextprime(p); a += p%4-2
    if a < 0: print(p, end = ', ') # _Ya-Ping Lu_, Jan 18 2025

