# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A323416

f = lambda n:+(n==0) or n*f(n-1)
def seq(n):
   if n==0: return
   l = []
   for i in range(1, n + 1):
       # following line with a string repeat
       # s = int('1'*i)
       s = 0
       for j in range(i):
           s += 10 ** j
       l += [s*f(i-1)]
   return l

