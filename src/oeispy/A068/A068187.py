# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A068187

from sympy import factorint
def A068187(n):
    if n == 1:
        return 1
    pf = factorint(n)
    return 0 if max(pf) > 7 else int(''.join(sorted(''.join(str(a)*(n*b) for a,b in pf.items()).replace('222','8').replace('22','4').replace('33','9')))) # _Chai Wah Wu_, Aug 13 2017

