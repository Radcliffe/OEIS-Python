# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A280642

i=0
j=1
while i<=874:
    n=str(i**3)
    l=len(n)
    if l%2 and n[(l-1)//2]=="2":
        print(str(i), end=', ')
        j+=1
    i+=1 # _Indranil Ghosh_, Mar 06 2017

