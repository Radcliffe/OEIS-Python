# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A045918

from re import finditer
def A045918(n):
    return int(''.join([str(len(m.group(0)))+m.group(0)[0] for m in finditer(r'(\d)\1*',str(n))]))
# _Chai Wah Wu_, Dec 03 2014

