# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A367834

from math import prod, factorial
def A367834(n): return (prod(i**8+j**8 for i in range(1,n) for j in range(i+1,n+1))*factorial(n)**4)**2<<n # _Chai Wah Wu_, Dec 02 2023

