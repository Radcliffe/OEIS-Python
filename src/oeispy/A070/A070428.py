# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A070428

from sympy import mobius, integer_nthroot
def A070428(n): return int(1-sum(mobius(x)*(integer_nthroot(10**n,x)[0]-1) for x in range(2,(10**n).bit_length()))) # _Chai Wah Wu_, Aug 13 2024

