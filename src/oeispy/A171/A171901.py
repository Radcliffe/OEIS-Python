# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A171901

def is_ok(n):
    s = str(n)
    return any(s[i] == s[i - 1] for i in range(1, len(s)))
A171901_list = [n for n in range(400) if is_ok(n)] # _Chai Wah Wu_, Feb 14 2019

