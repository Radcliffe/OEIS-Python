# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A258881

def ssd(n): return sum(int(d)**2 for d in str(n))
def a(n): return n + ssd(n)
print([a(n) for n in range(63)]) # _Michael S. Branicky_, Jan 30 2021

