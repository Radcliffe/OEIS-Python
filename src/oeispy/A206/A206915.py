# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A206915

def A206915(n):
    l = n.bit_length()
    k = l+1>>1
    return (n>>l-k)-(int(bin(n)[k+1:1:-1] or '0',2)>(n&(1<<k)-1))+(1<<k-1+(l&1^1)) # _Chai Wah Wu_, Jul 24 2024

