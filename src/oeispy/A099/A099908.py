# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A099908

from __future__ import division
A099908_list, b = [], 1
for n in range(1,10001):
    A099908_list.append(b % n**4)
    b = b*2*(2*n+1)//(n+1) # _Chai Wah Wu_, Jan 26 2016

