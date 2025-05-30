# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A280873

def A280873():
    yield 1
    for x in A280873():
        if ((x & 1) and (x > 1)):
            yield 2*x
        yield 2*x+1
def take(n, g):
  '''Returns a list composed of the next n elements returned by generator g.'''
  z = []
  if 0 == n: return(z)
  for x in g:
    z.append(x)
    if n > 1: n = n-1
    else: return(z)
take(120, A280873())
# _Antti Karttunen_, Oct 11 2017, after the given Mathematica-code (by _Floris Strijbos_) and a similar generator-example for A003714 by _David Eppstein_ (cf. "Self-recursive generators" link).

