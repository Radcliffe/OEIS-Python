# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A214250

SIZE=29  # must be odd
grid = [0] * (SIZE*SIZE)
saveX = [0]* (SIZE*SIZE)
saveY = [0]* (SIZE*SIZE)
saveX[1] = saveY[1] = posX = posY = SIZE//2
grid[posY*SIZE+posX]=1
n = 2
def walk(stepX,stepY,chkX,chkY,chkX2,chkY2):
  global posX, posY, n
  while 1:
    posX+=stepX
    posY+=stepY
    grid[posY*SIZE+posX]=n
    saveX[n]=posX
    saveY[n]=posY
    n+=1
    if posX==0 or grid[(posY+chkY)*SIZE+posX+chkX]+grid[(posY+chkY2)*SIZE+posX+chkX2]==0:
        return
while 1:
    walk(-1, 0,  1, -1, 0, -1)   # left
    if posX==0:
        break
    walk( 1,-1,  1, 1,  1, 1)    # right+up
    walk( 1, 1, -1,  0, -1, 0)   # right+down
for n in range(1,122):
    posX = saveX[n]
    posY = saveY[n]
    k = grid[(posY-1)*SIZE+posX] + grid[(posY+1)*SIZE+posX]
    k+= grid[(posY-1)*SIZE+posX-1] + grid[(posY-1)*SIZE+posX+1]
    k+= grid[(posY+1)*SIZE+posX-1] + grid[(posY+1)*SIZE+posX+1]
    k+= grid[posY*SIZE+posX-1] + grid[posY*SIZE+posX+1]
    print(k, end=' ')

