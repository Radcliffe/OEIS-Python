# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A257680

def a007623(n, p=2): return n if n<p else a007623(n//p, p+1)*10 + n%p
def a(n): return 1 if '1' in str(a007623(n)) else 0
print([a(n) for n in range(101)]) # _Indranil Ghosh_, Jun 21 2017

