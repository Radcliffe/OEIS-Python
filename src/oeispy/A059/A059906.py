# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A059906

def a(n):
    x=[int(t) for t in list(bin(n)[2:])[::-1]]
    return sum(x[2*i + 1]*2**i for i in range(int(len(x)//2)))
print([a(n) for n in range(105)]) # _Indranil Ghosh_, Jun 25 2017

