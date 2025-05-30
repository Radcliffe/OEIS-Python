# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A357073

def A357073(n):
    tlist, s, m = [1, 2], 0, n
    while (t:=tlist[-1]+tlist[-2]) <= n:
        tlist.append(t)
    for d in tlist[::-1]:
        s = (s<<1)%n
        if d <= m:
            s = (s+1)%n
            m -= d
    return s # _Chai Wah Wu_, Sep 11 2022

