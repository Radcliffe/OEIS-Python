# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A346007

from sympy import binomial
def A346007(n):
    i = (5-n)%5
    return binomial(5,i+1)*((n+i)//5)**(i+1) # _Chai Wah Wu_, Jul 25 2021

