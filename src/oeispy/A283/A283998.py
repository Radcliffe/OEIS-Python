# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A283998

def A(n): return 2*n - bin(2*n)[2:].count("1")
print([n&A(n//2) for n in range(101)]) # _Indranil Ghosh_, Mar 25 2017

