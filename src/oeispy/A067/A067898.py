# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A067898

def A067898(n):
    s = set(str(n))
    for i in range(10):
        if str(i) not in s:
            return i
    return 10 # _Chai Wah Wu_, Apr 13 2024

