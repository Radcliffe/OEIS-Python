# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A331560

# Palindrome-free interval about 196 offsets. Slow brute-force
n = 196
while n < 10**15:
     m = n
     while m != int(str(m)[::-1]): m+=1
     s = m
     m = n
     while m != int(str(m)[::-1]): m-=1
     print(s-m)
     n = n + int(str(n)[::-1])

