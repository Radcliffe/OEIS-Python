# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A065515

from sympy import primepi
from sympy.ntheory.primetest import integer_nthroot
def A065515(n): return 1+sum(primepi(integer_nthroot(n,k)[0]) for k in range(1,n.bit_length())) # _Chai Wah Wu_, Jul 23 2024

