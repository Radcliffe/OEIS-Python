# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A371003

from math import comb
def A371003(n): return comb((n<<1)-1,n)-n-((m:=(n-1)**2)*(m+3)>>2) # _Chai Wah Wu_, Mar 29 2024

