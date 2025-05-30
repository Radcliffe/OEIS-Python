# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A367805

from itertools import count, dropwhile
from sympy import prime, isprime
def A367805(n):
    if n==1:
        return 0
    else:
        p = prime(n)
        return next(dropwhile(lambda x:not isprime(x*p+2),count(1))) # _Chai Wah Wu_, Jan 04 2024

