# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A099377

from sympy import gcd, divisor_sigma
def A099377(n): return (lambda x, y: y*n//gcd(x,y*n))(divisor_sigma(n),divisor_sigma(n,0)) # _Chai Wah Wu_, Oct 20 2021

