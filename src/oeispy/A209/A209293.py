# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A209293

t=int((math.sqrt(8*n-7) - 1)/ 2)
i=n-t*(t+1)/2
j=(t*t+3*t+4)/2-n
m1=int((i+j)/2)+int(i/2)*(-1)**(i+t+1)
m2=int((i+j+1)/2)+int(i/2)*(-1)**(i+t)
m=(m1+m2-1)*(m1+m2-2)/2+m1

