# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A284599

from sympy import divisors, isprime
def a(n): return sum([i for i in divisors(n) if isprime(i) and (isprime(i - 2) or isprime(i + 2))])
print([a(n) for n in range(1, 91)]) # _Indranil Ghosh_, Mar 30 2017

