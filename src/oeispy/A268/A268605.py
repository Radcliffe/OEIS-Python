# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A268605

sumprime = 0
isPrime=lambda x: all(x % i != 0 for i in range(int(x**0.5)+1)[2:])
print(0)
for i in range(2,100):
  if isPrime(i):
    alfa = ""
    k = i + sumprime
    sumprime = k
    while k > 9:
      alfa = alfa + "9"
      k = k - 9
    alfa = str(k)+alfa
    print(alfa)

