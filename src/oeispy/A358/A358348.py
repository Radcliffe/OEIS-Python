# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A358348

def A358348(n):
    return ((0, 1, 4, 7, 9, 10, 13, 16, 17)[m := n % 9]
         + (n - m << 1))  # _Chai Wah Wu_, Feb 09 2023

