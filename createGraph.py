import newFeasibleEdge
import req

def createGraph(M,S,D):
    V = [S]
    E = []
    U = []
    vL = S
    U.insert(0, vL)

    simBlock = req.simulateBlock(M)

    #26,22
    while(req.isFeasible(6,vL,D,simBlock) != True):
        vY, vX = newFeasibleEdge.newFeasibleEdge( 36, V,simBlock )  # vY == S, vX == new Feasible point
        while(req.controlOverlap(V,vX) != True):
            vY, vX = newFeasibleEdge.newFeasibleEdge( 36, V, simBlock )  # vY == S, vX == new Feasible point



        if (req.isFeasible(6,U[0],vX,simBlock ) == True):
            V.append(vX)
            U.insert(0, vX)
            for x in range(len(V)):
                if(req.isFeasible(6,V[x],vX,simBlock)==True and vX != V[x]):
                    E.append([V[x], vX])
                    E.append([vX, V[x]])
            vL = vX

    temp = len(V)
    E.append([36,V[temp-1]])
    temp = len(V)
    E.append([V[temp-1],36])


    return E









