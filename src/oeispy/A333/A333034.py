# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A333034

def A333034(n):
    return sum(int(d) for i in range(10**(n-1),10**n) for d in str(i**2)) # _Chai Wah Wu_, Mar 05 2020

