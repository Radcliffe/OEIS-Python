# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A182469

from sympy import divisors
def row(n):
    return [d for d in divisors(n) if d % 2]
for n in range(1, 21): print(row(n)) # _Indranil Ghosh_, Apr 22 2017

