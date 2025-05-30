# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A214176

SIZE=11  # must be odd
grid = [0] * (SIZE*SIZE)
posX = posY = SIZE//2
grid[posY*SIZE+posX]=1
n = 2
saveX = [0]* (SIZE*SIZE+1)
saveY = [0]* (SIZE*SIZE+1)
saveX[1]=posX
saveY[1]=posY
def walk(stepX,stepY,chkX,chkY):
  global posX, posY, n
  while 1:
    posX+=stepX
    posY+=stepY
    grid[posY*SIZE+posX]=n
    saveX[n]=posX
    saveY[n]=posY
    n+=1
    if posX+posY==0 or grid[(posY+chkY)*SIZE+posX+chkX]==0:
        return
while 1:
    walk(0,-1, 1, 0)    # up
    if posX+posY==0:
        break
    walk(1, 0, 0, 1)    # right
    walk(0, 1,-1, 0)    # down
    walk(-1,0, 0,-1)    # left
for n in range(1,(SIZE-2)*(SIZE-2)+1):
    posX = saveX[n]
    posY = saveY[n]
    k = grid[(posY-1)*SIZE+posX] + grid[(posY+1)*SIZE+posX]
    k+= grid[(posY-1)*SIZE+posX-1] + grid[(posY-1)*SIZE+posX+1]
    k+= grid[(posY+1)*SIZE+posX-1] + grid[(posY+1)*SIZE+posX+1]
    print(k+grid[posY*SIZE+posX-1] + grid[posY*SIZE+posX+1], end=', ')

