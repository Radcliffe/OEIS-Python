# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A358119

from math import comb
def A358119(n): return sum((-1 if j&1 else 1)*comb((n<<1)-j,j)*comb(n-j<<1,n-j)*comb(n-j+2<<1,n-j+2)//(n-j+1)//(n-j+3) for j in range(n+1)) # _Chai Wah Wu_, Nov 11 2022

