import newFeasibleEdge
import req

def createGraph(M,S,D):
    V = [S]
    E = []
    U = []
    vL = S
    U.insert(0, vL)
    #26,22
    while(req.isFeasible(6,vL,D) != True):
        vY, vX = newFeasibleEdge.newFeasibleEdge( 36, V )  # vY == S, vX == new Feasible point
        while(req.controlOverlap(V,vX) != True):
            vY, vX = newFeasibleEdge.newFeasibleEdge( 36, V )  # vY == S, vX == new Feasible point


        for x in range(1):
            if (req.isFeasible(6,U[x],vX ) == True):
                V.append(vX)
                U.insert(0, vX)
                for x in range(len(V)):
                    if(req.isFeasible(6,V[x],vX)==True and vX != V[x]):

                        E.append([V[x], vX])
                vL = vX


    print("E:" , E)
    print("V:",V)
    print("U: :", U)

    """
    req.drawGraph(E)
    """

    return E









