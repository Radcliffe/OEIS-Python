# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A053067

def a(n): return int("".join(map(str, range((n-1)*n//2+1, n*(n+1)//2+1))))
print([a(n) for n in range(1, 16)]) # _Michael S. Branicky_, Jan 23 2021

