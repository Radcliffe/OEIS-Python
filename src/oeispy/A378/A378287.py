# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A378287

from sympy import integer_nthroot, mobius
def A378287(n):
    def f(x): return int(n+integer_nthroot(x,4)[0]-sum(mobius(k)*(integer_nthroot(x,k)[0]+integer_nthroot(x,k<<1)[0]-2) for k in range(3,x.bit_length())))
    m, k = n, f(n)
    while m != k: m, k = k, f(k)
    return m

