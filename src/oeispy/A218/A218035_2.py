# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A218035

def A218035(n): return 4 if n == 1 else (n**3-9*n**2+59*n-3)//24 if n % 2 else (n**3-6*n**2+32*n+48)//48 # _Chai Wah Wu_, Apr 03 2021

