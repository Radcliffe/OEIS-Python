# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A377466

from itertools import islice
from sympy import prime
from gmpy2 import is_power, next_prime
def A377466_gen(startvalue=1): # generator of terms >= startvalue
    k = max(startvalue,1)
    p = prime(k)
    while (q:=next_prime(p)):
        c = 0
        for i in range(p+1,q):
            if is_power(i):
                c += 1
                if c>1:
                    yield k
                    break
        k += 1
        p = q
A377466_list = list(islice(A377466_gen(),9)) # _Chai Wah Wu_, Nov 04 2024

