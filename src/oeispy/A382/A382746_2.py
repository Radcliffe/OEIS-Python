# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A382746

def A382746(n):
    def f(x): return n+x-sum((x>>m)+1>>1 for m in range(x.bit_length()+1) if m%6<3)
    m, k = n, f(n)
    while m != k: m, k = k, f(k)
    return m # _Chai Wah Wu_, Apr 10 2025

