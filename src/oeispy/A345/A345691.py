# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A345691

from statistics import pvariance
from sympy.core.numbers import igcdex
def A345691(n): return pvariance(n**2*(u**2+v**2) for u, v, w in (igcdex(x,y) for x in range(1,n+1) for y in range(1,n+1)))

