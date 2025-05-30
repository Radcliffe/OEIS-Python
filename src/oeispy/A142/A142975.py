# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A142975

def fib(arb1,arb2,nth):
    if nth == 0:
            return arb1
    if nth == 1:
            return arb2
    x = [0]*nth
    x[0] = arb1
    x[1] = arb2
    for i in range(2,nth,1):
            x[i] = x[i-1]+x[i-2]
    return x[-1]
def fib2d(n):
    return fib(1,fib(1,1,n),n)
[fib2d(i) for i in range(1,10)]
# the function fib2d will return the n-th term of the sequence.

