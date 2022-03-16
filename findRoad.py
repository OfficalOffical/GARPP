import manhattanDistance
import createGraph
import req
import random

def findPath(M,S,D,N):
    P = []
    counter = 0
    g = createGraph.createGraph(M,S,D)
    sortedG = req.sortingE(g)
    print(sortedG)
    vi = S

    for x in range(N+1):
        vi=1
        tempP = [S]
        counter = 0
        while(vi != g[(len(g)-1)][1] and counter < 100):
            tempMin, tempMax = findRange(g, vi)
            tempLast = random.randint(tempMin, tempMax)
            while ((req.controlOverlap(tempP, g[tempLast][1]) != True) and counter < 100):
                tempMin, tempMax = findRange(g, vi)
                tempLast = random.randint(tempMin, tempMax)
                counter += 1


            tempP.append(g[tempLast][1])
            vi =  g[tempLast][1]

            counter += 1

        if (tempP[len(tempP) - 1] == g[(len(g) - 1)][1]):
            P.append(tempP)


    for x in range(len(P)):
       print("P ",x+1,": ",P[x-1])
       manhattanDistance.ManhattanDistance(P[x-1])







def findRange(g,toFind):
    tempMin = 1000000
    tempMax = 0
    for x in range(len(g)):
        if(toFind == g[x][0]):
            if(x>tempMax):
                tempMax = x
            if(x<tempMin):
                tempMin=x
    return tempMin,tempMax




