# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A379152

from itertools import count, islice
def A379152_gen(): # generator of terms
    yield from [1,1]
    c, s = 1, 3
    for n in count(2):
        c = (c*((n<<2)-2))//(n+1)
        if n == s:
            yield c.bit_count()
            s = (s<<1)|1
A379152_list = list(islice(A379152_gen(),10)) # _Chai Wah Wu_, Dec 17 2024

