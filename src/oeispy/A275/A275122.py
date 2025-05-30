# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A275122

import numpy as np
# This is used for the terms[] array
numLayers = 22
# Number of layers that you want to generate
# Number of terms = numLayers^3
width = numLayers*2
# Width and height of the terms[] array
neighbors = [[0, 0], [0, 1], [1, 0], [1, 1], [1, 2], [2, 1], [2, 2]]
# Neighbors of terms that are added together
terms = np.zeros((numLayers, width, width))
# Initialize terms[] array with specified dimensions and fill it with zeros
terms[0][0][0] = 1
# Place a single 1 in layer 0
for l in range(1, numLayers):
  for x in range(width):
    for y in range(width):
      for n in neighbors:
        terms[l][x][y] += terms[l-1][x-n[0]][y-n[1]]
# Calculate terms
seq = terms.flatten().tolist()
# List containing all terms in array
while 0 in seq:
  seq.remove(0)
# Remove zeros from array
for s in range(len(seq)):
  seq[s] = int(seq[s])
# Turn all terms from floats to integers
final = ""
for s in range(len(seq)):
  final += str(s+1)+" "+str(seq[s])+"\n"
# Put the terms into a single string in b-file format
bfile = open("b275122.txt", "w")
bfile.write(final)
bfile.close()
# Write this string to the b-file

