# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A347325

def A347325(n):
    a = [i for i in range(1,n+1)]
    while len(a) != 1:
        del a[:len(a)+1:2]
        a.reverse()
    return a[-1] # _Marc Kouyoumdjian_, Dec 15 2021

