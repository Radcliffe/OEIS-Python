# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A236416

def Tri(x):
  for n in range(10**10):
    if x == n*(n+1)/2:
      return True
    if x < n*(n+1)/2:
      return False
  return False
def TriAve(init):
  print(init)
  lst = []
  lst.append(init)
  n = 1
  while n*(n+1)/2 < 10**10:
    if n*(n+1)/2 not in lst:
      if Tri(((sum(lst)+int(n*(n+1)/2))/(len(lst)+1))):
        print(int(n*(n+1)/2))
        lst.append(int(n*(n+1)/2))
        n = 1
      else:
        n += 1
    else:
      n += 1

