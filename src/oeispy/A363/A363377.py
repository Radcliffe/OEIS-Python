# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A363377

A363377=lambda n: (8+n%2*81)*10**(n>>1)//9 if n else 7
print([A363377(n) for n in range(30)]) # _Natalia L. Skirrow_, Jun 26 2023

