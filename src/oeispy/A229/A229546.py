# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A229546

def rev(n):
    return int(''.join(reversed(str(n))))
def DP(n):
    p = 1
    for i in str(n):
        p *= int(i)
    return p
{print(n,end=', ') for n in range(10**3) if rev(n+DP(n))==n+DP(n)}
# Simplified by _Derek Orr_, Mar 22 2015

