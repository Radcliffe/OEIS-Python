# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A066452

def A066452(n):
    return len([x for x in range(1,n) if all([x % d  for d in range(2,n) if (n % d) and (2*n) % d in [d-1,0,1]])]) # _Chai Wah Wu_, Aug 07 2014

