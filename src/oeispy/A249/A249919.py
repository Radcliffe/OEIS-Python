# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A249919

def A249919(n):
    x=bin(n)[2:]
    s=0
    for i in x:
        s+=[6,2][int(i)]
    return s # _Indranil Ghosh_, Feb 02 2017

