# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A375972

def genNextRow(arr):
    nextRow = []
    nextRow.append(arr[0])
    for i in range(1, len(arr)):
        nextRow.append(arr[i-1]+arr[i])
    nextRow.append(arr[len(arr)-1])
    return nextRow
pascal = [[1],[1,1]]
n = 0
index = 1
while n < 30:
    pascal.append(genNextRow(pascal[1]))
    pascal.pop(0)
    print(pascal[1][index])
    index = index + (pascal[1][index] % 2)
    n += 1

