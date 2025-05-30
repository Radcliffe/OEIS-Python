# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A290284

from fractions import Fraction
def FracSqrt(p):
    a = Fraction(p/1)
    b = Fraction(1/1)
    e = Fraction(10**(-200))
    while a-b > e:
        a = (a+b)/2
        b = p/a
    return a
print("number: ")
pp = int(input())
p = FracSqrt(pp)
n = 0
while n >= 0:
    n = n+1
    q = p.limit_denominator(n)
    if (n == 1) or (q != q0):
        t = q*n
        m = t*t-pp*n*n
        print(n,q,m)
    q0 = q

