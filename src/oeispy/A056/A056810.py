# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A056810

def ispal(n): s = str(n); return s == s[::-1]
def afind(limit):
    for k in range(limit+1):
        if ispal(k**4): print(k, end=", ")
afind(10000001) # _Michael S. Branicky_, Sep 05 2021

