# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A124980

from sympy import divisors, isprime, prod
def PD(n, L=None): return [[]] if n==1 else [
    [d]+P for d in divisors(n)[:0:-1] if d <= (L or n) for P in PD(n//d, d)]
A2144=lambda upto=999: filter(isprime, range(5, upto, 4))
def A124980(n):
    return min(prod(a**(f-1) for a,f in zip(A2144(), P))
               for P in PD(n*2, n)+PD(n*2-1)) # _M. F. Hasler_, Jul 07 2024

