# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A263194

def ok(n): return (n//100) + (n%100) == (n//10)%100
print([m for m in range(10000) if ok(m)]) # _Michael S. Branicky_, Jan 25 2021

