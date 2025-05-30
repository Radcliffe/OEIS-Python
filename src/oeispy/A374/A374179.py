# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A374179

from sympy import nextprime
def A374179(n):
    p, pb = 2, 2
    while (q:=nextprime(p)):
        if pb==(qb:=q.bit_length()) and (p^q).bit_count() == n:
            return p
        p, pb = q, qb  # _Chai Wah Wu_, Jul 10 2024

