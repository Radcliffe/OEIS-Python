# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A329402

numbers=[]
for n in range(500):
    c=int(0)
    n=int(n+1)
    for x in range(2*n+1,4*n+1):
        y=(2*n*x)/(x-2*n)
        if y==y//1:
            y=int(y)
            c=c+1
    numbers.append(c)
print(numbers)

