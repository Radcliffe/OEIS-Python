# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A212315

def isa(n): return n.bit_count()==((n*(n+1))>>1).bit_count()
print(list(n for n in range(10**3) if isa(n)))  # _Dumitru Damian_, Mar 04 2023

