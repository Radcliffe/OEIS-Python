# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A340068

def a(n): return sum(bin(k)[2:].count("1")==3 for k in range(n+1, 2*n+1))
print([a(n) for n in range(1, 68)]) # _Michael S. Branicky_, Dec 28 2020

