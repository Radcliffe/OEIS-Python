# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A163599

from sympy import isprime
def a(n):
    s, k = str(n), 1
    while not str(k*(k+1)).startswith(s): k += 1
    return k*(k+1)
print([a(n) for n in range(1, 49)]) # _Michael S. Branicky_, Dec 02 2021

