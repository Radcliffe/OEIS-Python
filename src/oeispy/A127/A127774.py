# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A127774

from math import isqrt
from sympy.ntheory.primetest import is_square
def A127774(n): return (a:=(m:=isqrt(k:=n<<1))+(k>m*(m+1)))*(a+1)*(a+2)//6 if is_square((n<<3)+1) else 0 # _Chai Wah Wu_, Jun 09 2025

