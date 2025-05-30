# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A352653

def A352653(n):
    if n == 0: return 0
    m, g = 1, 0
    for k in range(n+1):
        g += m*n**2//(n+k)**2
        m *= ((n+k+1)*(n-k))**2
        m //= (k+1)**4
    return g>>1 # _Chai Wah Wu_, Oct 03 2022

