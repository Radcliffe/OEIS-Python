# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A094669

def f(x): return x//2 if x%2 == 0 else 3*x + 1
def a(n):
    i, c = 10**n, 0
    while i != 1: i, c = f(i), c+1
    return c
print([a(n) for n in range(1, 54)]) # _Michael S. Branicky_, Jun 25 2021

