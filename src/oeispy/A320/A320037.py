# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A320037

from re import split
def A320037(n):
    return int(''.join(d+'0' if '1' in d else d+'1' for d in split('(0+)|(1+)',bin(n)[2:]) if d != '' and d != None),2)

