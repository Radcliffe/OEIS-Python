# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A070939

def a(n): return len(bin(n)[2:])
print([a(n) for n in range(105)]) # _Michael S. Branicky_, Jan 01 2021

