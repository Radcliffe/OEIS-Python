# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A168294

def A168294(n):
    s, t = [int(d) for d in str(n)], [int(d) for d in str(n+1)]
    l, m = len(s), len(t)
    u = [0]*(l+m-1)
    for i in range(l):
        for j in range(m):
            u[i+j] = (u[i+j] + s[i]*t[j]) % 10
    return int("".join(str(d) for d in u)) # _Chai Wah Wu_, Jun 30 2020

