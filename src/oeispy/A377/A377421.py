# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A377421

from sympy import isprime
def ok(n): return (b:=bin(n)[2:]) != (br:=b[::-1]) and isprime(int(br, 2))
print([k for k in range(1, 143) if ok(k)]) # _Michael S. Branicky_, Oct 28 2024

