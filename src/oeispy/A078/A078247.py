# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A078247

def a(n):
    k = 1
    while  8*int(bin(k)[2:])%n: k += 1
    return 8*int(bin(k)[2:])
print([a(n) for n in range(1, 43)]) # _Michael S. Branicky_, Aug 08 2021

