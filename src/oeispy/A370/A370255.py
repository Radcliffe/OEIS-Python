# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A370255

def A370255(n):
    if n == 0: return 1
    m = n
    a, b = divmod(m,10)
    while not b:
        m = a
        a, b = divmod(m,10)
    return m**(10*n) # _Chai Wah Wu_, Feb 20 2024

