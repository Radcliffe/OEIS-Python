# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A369154

from itertools import count, islice
from sympy import nthroot_mod, isprime
def A369154_gen(): # generator of terms
    c, m = 1, 1
    for k in count(0):
        m *= 7
        r = sorted(nthroot_mod(1,6,m,all_roots=True))
        for i in count(0,m):
            for p in r:
                if isprime(i+p):
                    if i+p == c:
                        yield k
                    c = i+p
                    break
            else:
                continue
            break
A369154_list = list(islice(A369154_gen(),30)) # _Chai Wah Wu_, May 04 2024

