# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A188061

from gmpy2 import powmod, is_square, isqrt
from sympy import divisor_sigma
A188061_list = [n for n in range(1,10**4) if powmod(isqrt(n) if is_square(n) else n, int(divisor_sigma(n,0))//(1 if is_square(n) else 2), int(divisor_sigma(n,1))) == 1] # _Chai Wah Wu_, Mar 10 2016

