# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A033539

# function, demonstrating the reversal of the lists:
def myrev(lista):
  '''Reverses a list, in cumbersome way.'''
  if(len(lista) < 2): return(lista)
  else:
    tr = myrev(lista[1:])
    return([tr[0]]+myrev([lista[0]]+myrev(tr[1:])))

