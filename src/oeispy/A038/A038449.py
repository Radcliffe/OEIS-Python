# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A038449

from itertools import islice
def A038449_gen(): # generator of terms
    yield int(bin(n:=127)[2:])
    while True: yield int(bin((n:=n^((a:=-n&n+1)|(a>>1)) if n&1 else ((n&~(b:=n+(a:=n&-n)))>>a.bit_length())^b))[2:])
A038449_list = list(islice(A038449_gen(),20)) # _Chai Wah Wu_, Mar 11 2025

