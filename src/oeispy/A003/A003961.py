# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A003961

from sympy import factorint, prime, primepi, prod
def a(n):
    f=factorint(n)
    return 1 if n==1 else prod(prime(primepi(i) + 1)**f[i] for i in f)
[a(n) for n in range(1, 11)] # _Indranil Ghosh_, May 13 2017

