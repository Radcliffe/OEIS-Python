# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A340593

from itertools import count, islice
def A340593_gen(): # generator of terms
    a, ndict = 0, {0:0}
    yield 0
    for n in count(1):
        yield (a:= (a-m if a>=(m:=ndict[n]) and a-m not in ndict else a+m) if n in ndict else (a-n if a>=n and a-n not in ndict else a+n))
        ndict[a] = n
A340593_list = list(islice(A340593_gen(),30)) # _Chai Wah Wu_, Jun 29 2023

