# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A335951

from math import lcm
from itertools import count, islice
from sympy import simplify,sqrt,bernoulli
from sympy.abc import x
def A335951_T(n,k):
    z = simplify((bernoulli(2*n,(sqrt(8*x+1)+1)/2)-bernoulli(2*n,1))/(2*n)).as_poly().all_coeffs()
    return z[n-k]*lcm(*(d.q for d in z))
def A335951_gen(): # generator of terms
    yield from (A335951_T(n,k) for n in count(0) for k in range(n+1))
A335951_list = list(islice(A335951_gen(),20)) # _Chai Wah Wu_, May 16 2022

