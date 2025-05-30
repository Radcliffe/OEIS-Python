# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A005132

from itertools import count, islice
def A005132_gen(): # generator of terms
    a, aset = 0, set()
    for n in count(1):
        yield a
        aset.add(a)
        a = b if (b:=a-n)>=0 and b not in aset else a+n
A005132_list = list(islice(A005132_gen(),30)) # _Chai Wah Wu_, Sep 15 2022

