# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A350605

from itertools import chain, islice
def A350605_gen(): # generator of terms
    s = {1}
    while True:
        yield from sorted(s)
        s = set(chain.from_iterable((x,2*x+1,3*x+1) for x in s))
A350605_list = list(islice(A350605_gen(),30)) # _Chai Wah Wu_, Jan 12 2022

