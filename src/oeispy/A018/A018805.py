# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A018805

from sympy import sieve
def A018805(n): return 2*sum(t for t in sieve.totientrange(1,n+1)) - 1 # _Chai Wah Wu_, Mar 23 2021

