# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A249129

def a249129():
   seq = {0:1}
   acc = 0
   i = 0
   while True:
      if i in seq:
         if i+1 in seq:
            if 2*i not in seq:
               seq[2*i] = seq[i]+seq[i+1]
         elif 2*i in seq:
            seq[i+1] = seq[2*i]-seq[i]
         else:
            while acc in seq.values():
               acc += 1
            seq[i+1] = acc
            seq[2*i] = seq[i] + seq[i+1]
      else:
         while acc in seq.values():
            acc += 1
         seq[i] = acc
      yield seq[i]
      i += 1
# _Christian Perfect_, Dec 02 2014

