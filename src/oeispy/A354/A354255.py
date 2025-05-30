# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A354255

from math import gcd, prod
from itertools import count, islice
def agen(): # generator of terms
    alst, aset, mink = [1], {1}, 2
    for n in count(2):
        k, s = mink, n - n//2
        prodall = prod(alst[n-n//2-1:n-1])
        while k in aset or gcd(prodall, k) != 1: k += 1
        alst.append(k); aset.add(k)
        if k%2 == 0: yield k
        while mink in aset: mink += 1
print(list(islice(agen(), 9))) # _Michael S. Branicky_, May 23 2022

