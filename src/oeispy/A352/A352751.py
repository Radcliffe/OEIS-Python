# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A352751

def a(n, order=4):
    d, m = list(map(int, str(n))), [0]*order
    for di in d: m[di%order] += 1
    return int(str(len(d)) + "".join(map(str, m)))
print([a(n) for n in range(37)]) # _Michael S. Branicky_, Apr 01 2022

