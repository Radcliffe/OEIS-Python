# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A380934

def a(n):
    if n == 1: return 1
    b = bin(n)[2:]
    L = len(b)
    g = '0' * (L - 1) + bin(L)[2:]
    d = g + b[1:]
    return int(d,2)
print([a(n) for n in range(1,60)])

