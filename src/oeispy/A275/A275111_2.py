# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A275111

from functools import reduce
from sympy import prime
def A275111(n): return ((q:=prime(n+1))-1)*pow(reduce(lambda i,j:i*j%q,range(prime(n)+1,q),1),-1,q)%q # _Chai Wah Wu_, Feb 24 2023

