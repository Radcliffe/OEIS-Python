# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A368207

from math import isqrt
def A368207(n):
    c, r = 0, isqrt(n)
    for w in range(r+1):
        for x in range(w,r+1):
            wx = w*x
            if wx>n:
                break
            for y in range(x+1,r+1):
                for z in range(y,n+1):
                    yz = wx+y*z
                    if yz>n:
                        break
                    if yz==n:
                        m = 1
                        if w!=x:
                            m<<=1
                        if y!=z:
                            m<<=1
                        c+=m
    return c # _Chai Wah Wu_, Dec 19 2023

