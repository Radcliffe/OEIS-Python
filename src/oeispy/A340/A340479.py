# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A340479

def A340479(n):
    s = str(n)
    return int(s[::-1]) + sum(int(d) for d in s) # _Chai Wah Wu_, Jan 09 2021

