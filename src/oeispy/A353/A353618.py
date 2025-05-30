# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A353618

from math import gcd
from itertools import count, islice
from sympy import integer_nthroot
def A353618_gen(): # generator of terms
    for b in count(1):
        q, c = 2, 8
        while c < b:
            d = (b-c)**2*(b+c)
            s, t = divmod(d,c)
            if t == 0:
                a, r = integer_nthroot(s,2)
                if r and b-c < a < b+c and gcd(a,b,q) == 1:
                    yield from (a, b, c)
            c += q*(3*q+3)+1
            q += 1
A353618_list = list(islice(A353618_gen(),30)) # _Chai Wah Wu_, May 14 2022

