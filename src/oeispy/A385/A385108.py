# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A385108

def a(n, k):
     return 4**k*(3*n**2-3*n+2)//2-3*n*sum(4**(k-j)*2**(j-1) for j in range(1,k+1))+ 3*sum(4**(k-j)*(2**(j-1)-1) for j in range(1,k+1))
for n in range(1, 10):
     row = [a(n, k)
for k in range(0, 10)]
     print(row)

