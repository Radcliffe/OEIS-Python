# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A083688

from sympy import bernoulli, harmonic
def a(n): return (bernoulli(2*n) * harmonic(2*n) / n).denominator
print([a(n) for n in range(1, 22)]) # _Indranil Ghosh_, Aug 04 2017

