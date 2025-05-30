# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A090946

def A090946(n):
    if n == 1: return 0
    def f(x):
        if x<=2: return n
        a, b, c = 1, 3, 0
        while b<=x:
            a, b = b, a+b
            c += 1
        return n+c
    m, k = n, f(n)
    while m != k: m, k = k, f(k)
    return m # _Chai Wah Wu_, Sep 10 2024

