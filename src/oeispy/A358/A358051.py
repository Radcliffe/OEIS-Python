# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A358051

from sympy.ntheory.factor_ import totient
from gmpy2 import *
def isok(k):
  if is_square(k):
    j = isqrt(k)
    a,b = iroot(totient(j) * j, 3)
    return b

