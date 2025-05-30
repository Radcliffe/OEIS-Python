# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A360450

def A360450(n, A=[0]):
   while n >= len(A):
      L = A[-1]; S = str(L); m = len(S); P = 10**m
      while M := L % P:
         P //= 10
         if M >= P and L - P not in A: L -= P; break
      else:
         P = 1; m = max(int(max(S)), m); M = 10**m
         while True:
            if L//P % 10 < m and L + P not in A: L += P; break
            P *= 10
            if P == M: M *= 10; P = 1
      A += [L]
   return A[n]

