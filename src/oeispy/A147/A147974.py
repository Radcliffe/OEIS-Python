# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A147974

def a(n): return n**3-((n-1)**3+(n-2)**3+(n-3)**3)
print([a(n) for n in range(1, 37)]) # _Michael S. Branicky_, Oct 08 2021

