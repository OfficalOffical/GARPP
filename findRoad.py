
import createGraph
import req
import random

def findPath(n):
    g = createGraph.createGraph(36,1,36)
    sortedG = req.sortingE(g)

    vi = 1

    print(sortedG)









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




