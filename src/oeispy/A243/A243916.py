# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A243916

from sympy import isprime
def a(n):
    if n<3: return 0
    i=2**n - 1
    while True:
        if isprime(i) and isprime((i - 1)/2): return i
        else: i-=2 # _Indranil Ghosh_, Jun 12 2017, after _Antti Karttunen_'s Scheme Code

