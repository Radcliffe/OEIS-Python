# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A360283

from math import factorial, lcm
def A360283(n): return factorial(n)*lcm(*(i for i in range(1,n+2)))//(n+1) # _Chai Wah Wu_, Feb 15 2023

