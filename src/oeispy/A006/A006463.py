# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A006463

from math import isqrt
def A006463(n): return (m:=isqrt((n<<3)+1)-1>>1)*(6*n-2-m*(m+3))//6 # _Chai Wah Wu_, Jun 07 2025

