# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A209400

#From recurrence
def a(n, adict={0:0, 1:0, 2:0, 3:0, 4:2, 5:7}):
 if n in adict:
  return adict[n]
 adict[n]=3*a(n-1)-a(n-2)-2*a(n-3)+a(n-4)-a(n-5)-2*a(n-6)
 return adict[n]

