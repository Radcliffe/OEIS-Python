# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A029747

def A029747(n):
    if n<3: return n
    a, b = divmod(n,3)
    return 1<<a+1 if b==1 else 3+b<<a-1 # _Chai Wah Wu_, Apr 02 2025

