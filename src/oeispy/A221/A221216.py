# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A221216

t=int((math.sqrt(8*n-7) - 1)/ 2)
i=n-t*(t+1)/2
j=(t*t+3*t+4)/2-n
result=((t+2)**2-2*(t+2)+4-(3*i+j-2)*(-1)**t)/2

