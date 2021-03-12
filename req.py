from random import randrange
import math
import bresenham


def optimization(V):

    for x in range(len(V)):
        if(V[x]==1):
            V.pop(x)
            return optimization(V)

    return V




def controlOverlap(arr,vX):
    if(vX == 1):
        return False
    for x in range(len(arr)):
        if(vX == arr[x]):
            return False
    return True

def toTransport(maxX, arr):
    c = []

    for x in range( len( arr ) ):
        temp, temp2 = arr[x]
        lastV = ((temp2-1)*maxX)+temp
        c.append( lastV )

    return c


def deTransport(maxX,num):
    tempX = num % maxX
    tempY = int( num / maxX ) + 1

    if (tempX == 0):
        tempX = maxX
        tempY -= 1

    return tempX, tempY



def maxDist(maxX, x, y):
    x0,y0 = deTransport( maxX, x )
    x1,y1 = deTransport( maxX, y )

    tempX = abs(x0-x1)
    tempY = abs(y0-y1)

    tempX *= tempX
    tempY *= tempY

    return math.sqrt(tempX+tempY)

def isFeasible(maxSize,start,end):  # O(N^2) look at this <<<<<<<<<<<
    block = [2,8,12,14,23,27,29,33,35]

    x0,y0 = deTransport(6,start)
    x1,y1 = deTransport(6,end)

    cT = bresenham.bresenham( x0, y0, x1, y1 )
    cF = toTransport(6,cT)

    for x in range(len(block)):
        for y in range(len(cF)):
            if(block[x]==cF[y]):
                return False

    return True








