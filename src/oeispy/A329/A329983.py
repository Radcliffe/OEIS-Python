# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A329983

def k(a,b):
    return ((a*b)%(a+b))
numberList=[]
def repeat(a):
    i=1
    while a!=0:
        a= k(a,i)
        i=i+1
    numberList.append(i)
for x in range(10000):
    repeat(x)
print(numberList)

