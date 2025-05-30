# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A382850

from itertools import count
def A382850_generator():
    k = C0 = C = 1
    for n in count(2):
        C0 = 2*C0 if n%2 == 1 else (n-1)*C0//(n//2) # C(n-1,floor((n-1)/2))
        C = C*n//(n-k) # C(n,k)
        if C <= C0:
            C = C*(n-k)//(k+1)
            k += 1
        yield k # _Pontus von Brömssen_, Apr 15 2025

