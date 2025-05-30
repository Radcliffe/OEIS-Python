# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A381330

from math import isqrt
from itertools import count, islice
from sympy import isprime, primerange
def A381330_gen(startvalue=1): # generator of terms >= startvalue
    for n in count(max(startvalue,1)):
        c = 0
        for p in primerange(isqrt(n)+1):
            if isprime(n-p**2):
                c += 1
            if c>1:
                yield n
                break
A381330_list = list(islice(A381330_gen(),30))

