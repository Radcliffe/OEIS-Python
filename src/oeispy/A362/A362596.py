# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A362596

from math import comb
def A362596(n): return ((n*(n-3)+4)*comb(n<<1,n)//(n+1)>>2)+(1<<(n<<1)-3) if n>1 else 1 # _Chai Wah Wu_, Apr 27 2023

