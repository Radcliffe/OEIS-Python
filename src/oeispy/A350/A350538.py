# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A350538

def a(n):
    m, inc = 2*n, n if n%2 == 0 else 2*n
    while not set(str(m)) <= set("02468"): m += inc
    return m
print([a(n) for n in range(1, 60)]) # _Michael S. Branicky_, Jan 05 2022

