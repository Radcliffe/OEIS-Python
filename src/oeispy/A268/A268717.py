# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A268717

def A003188(n): return n^(n//2)
def A006068(n):
    if n<2: return n
    m = A006068(n//2)
    return 2*m + (n%2 + m%2)%2
def a(n): return 0 if n<1 else A003188(1 + A006068(n - 1))
print([a(n) for n in range(0, 101)]) # _Indranil Ghosh_, Mar 31 2017

