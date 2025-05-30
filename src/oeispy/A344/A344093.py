# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A344093

terms = [1]
previous = 1
def isValid(num):
  counter = 0
  for possibleDiv in range(1, int(math.sqrt(num)) + 1):
    if num % possibleDiv == 0:
      counter += 1
      if num/possibleDiv % possibleDiv == 0 and possibleDiv != 1:
        return False
    if counter > 2:
      return False
  if counter == 2:
    return True
  return False
def generateSequence(numOfTerms):
  for i in range(numOfTerms):
    testNum = 1
    valid = False
    while not valid:
      if testNum not in terms:
        possibleNum = previous + testNum
        if isValid(num):
          valid = True
          terms.append(testNum)
          previous = testNum
      testNum += 1

