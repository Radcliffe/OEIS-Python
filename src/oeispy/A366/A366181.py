# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A366181

def A366181(n):
    a, b, c, d = 10**(n-1), 10**n, 10**((n<<1)-1), 10**(n<<1)
    return len({i*j for i in range(a,b) for j in range(min(i,c//i),min(b,d//i+1)) if c<=i*j<d}) # _Chai Wah Wu_, Oct 13 2023

