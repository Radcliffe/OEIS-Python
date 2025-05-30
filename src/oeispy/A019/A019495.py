# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A019495

from itertools import islice
def A019495_gen(): # generator of terms
    a, b = 4, 11
    yield from (a,b)
    while True:
        a, b = b, (b**2-1)//a
        yield b
A019495_list = list(islice(A019495_gen(),30)) # _Chai Wah Wu_, Dec 06 2023

