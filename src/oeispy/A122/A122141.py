# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A122141

from sympy.core.power import isqrt
from functools import cache
@cache
def T(d, n):
  if n == 0: return 1
  if n < 0 or d < 1: return 0
  return T(d-1, n) + sum(T(d-1, n-(j**2)) for j in range(1, isqrt(n)+1)) * 2  # _Darío Clavijo_, Feb 06 2024

