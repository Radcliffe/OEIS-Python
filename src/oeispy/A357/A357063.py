# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A357063

number_of_terms=38
def Cn(X):
    l=len(X)
    cn=1
    for i in range(1,int(l/2)+1):
        j=i
        while(X[l-j-1]==X[l-j-1+i]):
            j=j+1
            if j>=l:
                break
        candidate=int(j/i)
        if candidate>cn:
            cn=candidate
    return cn
# This algorithm generates a prefix of the level-3 Gijswijt sequence
def Generate_A3(number):
  glue_lengths=[]
  A3=[3]
  S=[3]
  i=0
  while(True):
      c=Cn(A3)
      if c<3:
        glue_lengths.append(len(S))
        i=i+1
        if i==number:
            break
        S=[]
      A3.append(max(c,3))
      S.append(max(c,3))
  return glue_lengths
glue_lengths=Generate_A3(number_of_terms-1)
beta_lengths=[1]
beta_length=1
for l in glue_lengths:
    beta_length=3*beta_length+l
    beta_lengths.append(beta_length)
print(beta_lengths)

