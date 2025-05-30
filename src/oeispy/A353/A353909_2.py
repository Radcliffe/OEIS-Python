# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A353909

from sympy import sqrt, divisors, totient
from sympy.ntheory.factor_ import core
def a(n):
  return -n if n & 1 == 1 else int(n * sum(totient(d) * sqrt(d // core(d)) / d for d in divisors(n) if d & 1 == 0))
 # _Darío Clavijo_, Dec 29 2022

