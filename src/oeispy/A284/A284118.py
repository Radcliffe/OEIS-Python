# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A284118

from sympy import divisors
from sympy.ntheory.factor_ import core
def a(n): return sum([i for i in divisors(n) if core(i)==i and isprime(i)==0]) # _Indranil Ghosh_, Mar 21 2017

