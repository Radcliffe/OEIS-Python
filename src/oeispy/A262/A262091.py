# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A262091

# print pairs with leading zeros
from __future__ import print_function
from itertools import combinations_with_replacement
for m in range(2,11):
    fs = '0'+str(m+1)+'d'
    for c in combinations_with_replacement(range(10),m+1):
        n = sum(d**m for d in c)
        r = sum(int(q)**m for q in str(n))
        rlist = sorted(int(d) for d in str(r))
        rlist = [0]*(m+1-len(rlist))+rlist
        if n < r and rlist == list(c):
            print(format(n,fs),format(r,fs)) # _Chai Wah Wu_, Jan 04 2016

