# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A335940

import numpy as np
def primeFactors(n):
    x=[]
    while n % 2 == 0:
        x.append(2),
        n = n / 2
    for i in range(3,int(np.sqrt(n))+1,2):
        while n % i== 0:
            x.append(i),
            n = n / i
    if n > 2:
        x.append(n)
    if len(x)==0:
        x.append(1)
    if len(x)!=1:
        y=x[-1]-x[0]
    else:
        y=x[0]
    return y
    print(len(x))
nums = list(range(1,101))
final=[]
for i in nums:
    final.append(primeFactors(i))
final = [int(i) for i in final]
print(final)

