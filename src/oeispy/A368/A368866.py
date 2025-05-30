# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A368866

from itertools import count
from sympy.ntheory.factor_ import digits
def A368866(n):
    k = 1
    for m in count(1):
        k <<= 1
        s = digits(k,n)[1:]
        if any(s[i]==s[i+1] for i in range(len(s)-1)):
            return m # _Chai Wah Wu_, Jan 08 2024

