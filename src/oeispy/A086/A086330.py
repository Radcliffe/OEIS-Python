# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A086330

def A086330(n):
    a, c = 0, 1
    for m in range(2,n):
        c = c*m%n
        if c==0:
            break
        a += c
    return a # _Chai Wah Wu_, Apr 16 2024

