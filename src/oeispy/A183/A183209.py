# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A183209

def a(n):
    if n==1: return 1
    if n%2==0: return 3*a(n//2) - 1
    else: return (3*a((n - 1)//2 + 1))//2
print([a(n) for n in range(1, 101)]) # _Indranil Ghosh_, Jun 06 2017

