# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A346953

from sympy import divisors
def f(n): return sum(d%10 == 3 for d in divisors(n)[1:-1])
def A346950upto(lim): return sorted(set(a*b for a in range(3, lim//3+1, 10) for b in range(a, lim//a+1, 10)))
print(list(map(f, A346950upto(2129)))) # _Michael S. Branicky_, Aug 11 2021

