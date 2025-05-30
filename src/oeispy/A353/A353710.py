# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A353710

from itertools import count, islice
def A353710_gen(): # generator of terms
    s, a, b, c, ab = {0,1}, 0, 1, 2, 1
    yield from (0,1)
    while True:
        for n in count(c):
            if not (n & ab or n in s):
                yield c
                a, b = b, n
                ab = a|b
                s.add(n)
                while c in s:
                    c += 1
                break
A353710_list = list(islice(A353710_gen(),20)) # _Chai Wah Wu_, May 10 2022

