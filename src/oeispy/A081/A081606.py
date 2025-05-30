# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A081606

from itertools import count, islice
def A081606_gen(): # generator of terms
    a = 0
    for n in count(1):
        b = int(bin(n)[2:],3)<<1
        yield from range(a+1,b)
        a = b
A081606_list = list(islice(A081606_gen(),30)) # _Chai Wah Wu_, Oct 13 2023

