# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A283187

def a(n):
    if n==0 or n==1: return n
    if n%2==0: return int(2*a(n/2))
    else: return int(a((n-1)/2)+(-1)**a((n+1)/2)) # _Indranil Ghosh_, Mar 03 2017

