# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A001523

def b(n, i):
    if i>n: return 0
    if n%i==0: x=1
    else: x=0
    return x + sum([b(n - i*j, i + 1)*(j + 1) for j in range(n//i + 1)])
def a(n): return 1 if n==0 else b(n, 1) # _Indranil Ghosh_, Jun 09 2017, after Maple code by _Alois P. Heinz_

