# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A069192

def A069192(n):
    s=0
    for i in range(1,n+1):
        if n%i==0: s+=int(str(i)[::-1])
    return s # _Indranil Ghosh_, Feb 10 2017

