# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A371124

from sympy.core.power import isqrt
from sympy.ntheory.primetest import is_square
def a(n):
  x = isqrt(n)
  while True:
    for y2 in range(x**2-n, -1, -n):
      if is_square(y2): return isqrt(y2)
    x+=1
print([a(n) for n in range(1, 79)])

