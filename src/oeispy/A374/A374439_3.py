# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A374439

def P(n, x):
    if n < 0: return P(n, x)
    return sum(T(n, k)*x**k for k in range(n + 1))
def sgn(x: int) -> int: return (x > 0) - (x < 0)
# Table of interpolated sequences
print("|  n | A039834 & A000045 | A000032 |   A000129   |   A048654  |")
print("|  n |     -P(n,-1)      | P(n,1)  |2^n*P(n,-1/2)|2^n*P(n,1/2)|")
print("|    |     Fibonacci     |  Lucas  |     Pell    |    Pell*   |")
f = "| {0:2d} | {1:9d}         |  {2:4d}   |   {3:5d}     |    {4:4d}    |"
for n in range(10): print(f.format(n, -P(n, -1), P(n, 1), int(2**n*P(n, -1/2)), int(2**n*P(n, 1/2))))

