# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A322523

def A322523(n):
    c, m = 0, n
    while not (a:=divmod(m,3))[1]:
        c += 1
        m = a[0]
    if m==2 or m%3==1: return c
    m = (m+1)//3-2
    while (a:=divmod(m,3))[1]:
        c += 1
        m = a[0]
    return c+1 # _Chai Wah Wu_, Oct 15 2022

