# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A359208

def f(n): return 1 if n == 0 else (m:=3*n)^((1 << m.bit_length())-1)
def a(n):
    i, fi, m = 0, n, n
    while fi != 0: i, fi, m = i+1, f(fi), max(m, fi)
    return m
print([a(n) for n in range(33)]) # _Michael S. Branicky_, Dec 20 2022

