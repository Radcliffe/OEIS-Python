# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A381129

from num2words import num2words as n2w
def f(n): return sum(1 for c in n2w(n).replace(" and", "") if c.isalpha())
def a(n):
    c, i, J = 1, 0, list(range(1, n+1))
    while len(J) > 1:
        q = J.pop(i)
        i = (i + f(c))%len(J)
        c = c+1
    return J[0]
print([a(n) for n in range(1, 75)]) # _Michael S. Branicky_, Feb 16 2025

