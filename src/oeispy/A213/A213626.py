# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A213626

def A213626(n): return sum((-1 if (i&(i>>1)).bit_count()&1 else 1)*sum((-1 if (j&(j>>1)).bit_count()&1 else 1)*sum(-1 if (k&(k>>1)).bit_count()&1 else 1 for k in range(j+1,n+1)) for j in range(i+1,n+1)) for i in range(n+1)) # _Chai Wah Wu_, Feb 12 2023

