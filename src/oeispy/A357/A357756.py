# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A357756

def sd(n): return sum(map(int, str(n)))
def a(n):
    k = 1
    while not sd(n*k) == sd((n*k)**2): k += 1
    return k
print([a(n) for n in range(75)]) # _Michael S. Branicky_, Oct 13 2022

