# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A256961

def flip(i,n):
  m = i%n
  m2 = n-m-1
  return i-m+m2
def revert(i,moves):
  for move,leader in reversed(moves):
    if i==leader-1:
      i=0
    else:
      i+=1
    i = flip(i,move)
  return i+3
def a256961():
  moves = []
  while True:
    move = revert(0,moves)
    leader = revert(move-1,moves)
    out = revert(flip(leader,move),moves)
    yield out
    moves.append((move,leader))
# _Christian Perfect_, Apr 20 2015

