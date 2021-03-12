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
                E.append([U[x],vX])
                V.append(vX)
                U.insert(0, vX)
                vL = vX


    print("V:",V)
    print("U: :", U)
    print("E:",E)








