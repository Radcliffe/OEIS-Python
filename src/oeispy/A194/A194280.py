# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A194280

t=int(math.sqrt(n-1))+1
i=(t % 2)*min(t,n-(t-1)**2) + ((t+1) % 2)*min(t,t**2-n+1)
j=(t % 2)*min(t,t**2-n+1) + ((t+1) % 2)*min(t,n-(t-1)**2)
m=(i+j-1)*(i+j-2)/2+j

