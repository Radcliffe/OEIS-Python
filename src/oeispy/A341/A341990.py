# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A341990

from math import gcd
def fourth_root(n):
    u, s = n, n + 1
    while u < s:
        s = u
        t = 3 * s + n // (s ** 3)
        u = t // 4
    return s
def a(n):
    N = 10 ** n
    L = fourth_root(N) * 3
    cnt = 0
    for a in range(1, L + 1):
       a2 = a * a
       for b in range(1, a):
           if (a + b) % 2 == 1 and gcd(a, b) == 1:
               b2 = b * b
               v = (4 * a * b + a2) * a2 - b2 * b2
               if v > N:
                   continue
               cnt += 1
    return cnt

