# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A046268

from sympy import isprime
def a(n):
    s = str(2**n)
    ss = (int(s[i:j]) for i in range(len(s)) for j in range(i+1, len(s)+1))
    return max((k for k in ss if isprime(k)), default=0)
print([a(n) for n in range(46)]) # _Michael S. Branicky_, Sep 20 2022

