# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A137515

from math import asin, sqrt, pi
hyp=2
som=0
n=1
while n<500:
    if som+asin(1/sqrt(hyp))/pi*180>n*360:
        print(hyp-2, end=', ')
        n=n+1
    som=som+asin(1/sqrt(hyp))/pi*180
    hyp=hyp+1

