# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A337988

from sympy import divisors, integer_nthroot
A337988_list = []
for n in range(1,10**6):
    for d in divisors(n):
        if 2*d*d >= n:
            break
        a, b = integer_nthroot(n-d*d,2)
        if b and n % a == 0:
            A337988_list.append(n)
            break # _Chai Wah Wu_, Oct 30 2020

