# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A183544

from itertools import islice
def A183544_gen(): # generator of terms
    a, b, i = 1, 1, 0
    while True:
        yield from (j+a for j in range(i,i+a))
        i += a
        a, b = b, a+b
A183544_list = list(islice(A183544_gen(),30)) # _Chai Wah Wu_, Oct 13 2022

