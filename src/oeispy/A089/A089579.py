# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A089579

from sympy import mobius, integer_nthroot
def A089579(n): return int(sum(mobius(x)*(1-integer_nthroot(10**n,x)[0]) for x in range(2,(10**n).bit_length())))-1 if n>1 else 3 # _Chai Wah Wu_, Aug 13 2024

