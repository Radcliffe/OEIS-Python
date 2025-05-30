# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A376613

def a(n):
    if n == 1: return 0
    s, t, n1 = 1, 0, (n - 1)
    while s < n:
        d = s << 1
        for l in range(0, n, d):
            m,r = min(l - 1 + s, n1), min(l - 1 + d, n1)
            t = (t << 1) + int(m < r)
        s = d
    return t
print([a(n) for n in range (1,22)])

