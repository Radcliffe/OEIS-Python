# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A005203

def A005203(n):
    s = '0'
    for i in range(n):
        s = s.replace('0','a').replace('1','10').replace('a','1')
    return int(s,2) # _Chai Wah Wu_, Apr 24 2025

