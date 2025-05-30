# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A369790

from collections import Counter
def A369790(n):
    c = {0:1}
    for k in range(1,n+1):
        d = Counter(c)
        for j in c:
            a = c[j]
            d[j+k] -= 3*a
            d[j+2*k] += 3*a
            d[j+3*k] -= a
        c = d
    return len(set(c.values()))+int(max(c)+1>len(c)) # _Chai Wah Wu_, Feb 01 2024

