# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A328447

def A328447(n):
    if n == 0: return 0
    s = str(n)
    l, s = len(s), ''.join(sorted(s.replace('0','')))
    return int(s[0]+'0'*(l-len(s))+s[1:]) # _Chai Wah Wu_, Dec 06 2021

