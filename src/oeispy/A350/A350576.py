# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A350576

def a(n):
    m = 2
    while n%m == 0: m += 1
    return n//(m-1) - (m-1)
print([a(n) for n in range(1, 76)]) # _Michael S. Branicky_, Jan 07 2022

