# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A348412

from sympy import gcd, divisor_sigma
A348412_list = [2*n for n in range(1,10**3) if (lambda x, y: 2*gcd(x,y*n)>=x)(divisor_sigma(n),divisor_sigma(n,0))] # _Chai Wah Wu_, Oct 20 2021

