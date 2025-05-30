# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A272369

from sympy import divisors, isprime
A272369_list = []
for i in range(92, 10**6, 92):
    for d in divisors(i):
        if d not in (1,2,4,46) and isprime(d+1):
            break
    else:
        A272369_list.append(i) # _Chai Wah Wu_, May 02 2016

