# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A168221

def A006368(n):
    if n%2 == 0:
        return 3*(n//2)
    elif n%4 == 1:
        return 3*(n//4)+1
    else:
        return 3*(n+1)//4-1
n = 0
while n < 30:
    print(n,A006368(A006368(n)))
    n = n+1 # _A.H.M. Smeets_, Aug 14 2019

