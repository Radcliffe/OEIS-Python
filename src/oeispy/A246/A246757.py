# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A246757

from operator import mul
from functools import reduce
def A246757(n):
    for i in range(10**n-1,int('1'*n)-1,-1):
        pd = reduce(mul,(int(d) for d in str(i)))
        if pd and not i % pd:
            return i # _Chai Wah Wu_, Sep 08 2014

