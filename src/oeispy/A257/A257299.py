# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A257299

from itertools import permutations
A257299_list = []
for n in permutations('123456789',9):
    x = 0
    for d in n:
        q, r = divmod(x,int(d))
        if r:
            break
        x = int(d + str(q))
    else:
        A257299_list.append(x)
A257299_list = sorted(A257299_list) # _Chai Wah Wu_, May 11 2015

