# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A126933

from itertools import count, islice
def A126933_gen(): # generator of terms
    a, b = 2, 10
    for n in count(1):
        a+=b if (c:=a>>n)&1 else b<<1
        b *= 10
        yield c
A126933_list = list(islice(A126933_gen(),20)) # _Chai Wah Wu_, Mar 16 2023

