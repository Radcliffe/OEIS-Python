# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A110904

from __future__ import division
mmax = 10**3
tmax, A110904_dict = mmax*(mmax+1)//2, {}
ti = 0
for i in range(1,mmax+1):
    ti += i
    p = ti*i*(i-1)//2
    for j in range(i,mmax+1):
        p += ti*j
        if p <= tmax:
            A110904_dict[p] = A110904_dict[p]+1 if p in A110904_dict else 1
        else:
            break
A110904_list = sorted([i for i in A110904_dict if A110904_dict[i] == 3]) # _Chai Wah Wu_, Nov 29 2015

