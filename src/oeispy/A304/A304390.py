# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A304390

nmax=10000
def is_prime(num):
    if num == 0 or num == 1: return(0)
    for k in range(2, num):
       if (num % k) == 0:
           return(0)
    return(1)
ris = ""
for i in range(nmax):
    r=int((str(i)[::-1]))
    t=pow(i,2)+pow(r,2)
    if is_prime(i):
       if is_prime(t):
          ris = ris+str(i)+","
print(ris)

