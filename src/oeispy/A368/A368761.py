# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A368761

def f(n): return 1+sum((2**k-1)*2**((n-1-k)*k) for k in range(1,n))

