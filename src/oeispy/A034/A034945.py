# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A034945

def a034945(n):
    ary=[0]
    a, mod=3, 7
    while len(ary) - 1<n:
        b=a%mod
        if b!=ary[-1]: ary.append(b)
        a=b**2 + b - 2
        mod*=7
    return ary
print(a034945(100)) # _Indranil Ghosh_, Aug 03 2017, after Ruby

