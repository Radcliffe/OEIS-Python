# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A059009

i=j=0
while j<=800:
    if bin(i)[2:].count("0")%2:
        print(str(j)+" "+str(i))
        j+=1
    i+=1 # _Indranil Ghosh_, Feb 04 2017

