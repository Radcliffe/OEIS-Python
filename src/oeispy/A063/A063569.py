# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A063569

def A063569(n):
    m, k, s = 1, 6, str(n)
    while s not in str(k):
        m += 1
        k *= 6
    return m # _Chai Wah Wu_, Nov 14 2019

