# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A281015

# uses[A280913]
from sympy import isprime
i=0
j=1
while j<=100:
    if isprime(A280913(i)):
        print(str(j)+" "+str(i))
        j+=1
    i+=1

