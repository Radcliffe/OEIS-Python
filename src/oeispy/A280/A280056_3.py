# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A280056

from __future__ import division
def A280056(n):
    return (n**2 - (n % 2))*(n-1)*(n-2)//2 # _Chai Wah Wu_, Dec 25 2016

