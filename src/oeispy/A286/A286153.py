# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A286153

def T(a, b): return ((a + b)**2 + 3*a + b)//2
def A(n, k): return T(n^k, k) if n>k else T(n, n^k)
for n in range(1, 21): print([A(k, n - k + 1) for k in range(1, n + 1)]) # _Indranil Ghosh_, May 21 2017

