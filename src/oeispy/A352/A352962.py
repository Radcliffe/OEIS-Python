# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A352962

from math import gcd
from itertools import count, islice
def A352962_gen(): # generator of terms
    a = 2
    yield a
    for n in count(2):
        yield (a:= min(n,a) if gcd(n,a) == 1 else n+2)
A352962_list = list(islice(A352962_gen(),30)) # _Chai Wah Wu_, May 24 2022

