# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A064484

# Generate first twenty rows using recurrence
rows=[[2]]; row=[2]
for i in range(19):
  row=[(row[j]*(j+2)+sum(row[:j])*2) if (i+j)%2==1 else row[j]*(j+1) for j in range(i+1)]+[row[-1]*(i+2)]
  rows.append(row)
# _Andrew Woods_, Jun 18 2013

