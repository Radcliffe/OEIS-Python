# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A343087

from sympy import isprime,nextprime
primes=[2]
def solve(v,k,i,j):
    global record,stack,primes
    if k==0:
        if isprime(v+1):
            record=v
        return
    while True:
        if i>=len(primes):
            primes.append(nextprime(primes[-1]))
        if j<len(stack) and stack[j]<primes[i]:
            f=stack[j] ; j+=1
        else:
            f=primes[i] ; i+=1
        if record==None or v * f**k < record:
            stack.append(f**2)
            solve(v*f,k-1,i,j)
            stack.pop()
        else:
            return
def a343087(n):
    global record,stack
    record,stack = None,[]
    solve(1,n,0,0)
    return record+1
# _Bert Dobbelaere_, Apr 11 2021

