# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A284013

def a(n): return n if n<2 else (a(n//2) if n%2==0 else a((n - 1)//2) + a((n + 1)//2))
print([n - a(n) for n in range(101)]) # _Indranil Ghosh_, Mar 23 2017

