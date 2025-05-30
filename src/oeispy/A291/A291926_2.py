# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A291926

from sympy.ntheory.digits import digits
def a(n):
    b = bin(n)[2:]
    if b.strip('0') == '1': return int(n == 2)
    k = (len(b)-1)*(n-1)
    while len(set(digits(2**k, n)[1:])) != n: k += 1
    return k
print([a(n) for n in range(2, 65)]) # _Michael S. Branicky_, Oct 07 2021

