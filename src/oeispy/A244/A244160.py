# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A244160

from sympy import catalan
def a(n):
    if n==0: return 0
    i=1
    while True:
        if catalan(i)>n: break
        else: i+=1
    return i - 1
print([a(n) for n in range(101)]) # _Indranil Ghosh_, Jun 08 2017

