# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A175046

from re import split
def A175046(n):
    return int(''.join(d+'1' if '1' in d else d+'0' for d in split('(0+)|(1+)',bin(n)[2:]) if d != '' and d != None),2) # _Chai Wah Wu_, Sep 24 2018

