# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A161502

def A161502(n):
    s = bin(n)[2:]
    if s == s[::-1]:
        return 0
    for i in range(1,len(s)):
        if s[i:] == s[-1:i-1:-1]:
            return i # _Chai Wah Wu_, Aug 27 2021

