# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A066062

def sums(s): return set((si+sj) for i, si in enumerate(s) for sj in s[i:])
def b(i, n, s):
    if sums(s) >= set(range(n+1)): return 2**(n+1-i)
    if i > n: return 0
    return b(i+1, n, s) + b(i+1, n, s+[i])
def a(n): return b(0, n, [])
print([a(n) for n in range(15)]) # _Michael S. Branicky_, Jan 15 2022

