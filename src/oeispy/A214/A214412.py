# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A214412

prpr = 0
prev = 1
fib = [0]*100
for n in range(100):
    fib[n] = prpr
    curr = prpr+prev
    prpr = prev
    prev = curr
#print fib[n]
for n in range(777):
    i = 1
    yes = 0
    while i*i<=n:
        r = n - i*i
        if r in fib:
            yes = 1
            break
        i += 1
    if yes==0:
        print(n, end=', ')

