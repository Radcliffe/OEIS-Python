# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A211197

t=int((math.sqrt(8*n-7) - 1)/ 2)
i=n-t*(t+1)/2
j=(t*t+3*t+4)/2-n
result =2*i+((-1)**i)*(0.5 - (j-1) % 2) - 0.5

