# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A262092

from itertools import count, combinations_with_replacement, islice
def A262092_gen(): # generator of terms
    for m in count(2):
        for c in combinations_with_replacement(range(10),m+1):
            n = sum(d**m for d in c)
            r = sum(int(q)**m for q in str(n))
            rlist = sorted(int(d) for d in str(r))
            rlist = [0]*(m+1-len(rlist))+rlist
            if n < r and rlist == list(c):
                yield r
A262092_list = list(islice(A262092_gen(),10)) # _Chai Wah Wu_, Dec 31 2021

