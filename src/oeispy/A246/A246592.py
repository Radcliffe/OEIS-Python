# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A246592

def A246592(n):
    s = bin(n)[2:]
    for i in range(len(s)-1):
        if s[i:i+2] == '10':
            return int(s[:i]+'01'+s[i+2:], 2)
    else:
        return n # _Chai Wah Wu_, Sep 06 2014

