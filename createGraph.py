import newFeasibleEdge
import req

def createGraph(M,S,D):
    V = [S]
    E = []
    U = []
    vL = S

    #26,22
    while(req.isFeasible(6,vL,D) != True):
        vY, vX = newFeasibleEdge.newFeasibleEdge( 36, V )  # vY == S, vX == new Feasible point
        while(vX == 1 ):
            vY, vX = newFeasibleEdge.newFeasibleEdge( 36, V )  # vY == S, vX == new Feasible point
        U.insert(0,vL)
        for x in range(1):
            if (req.isFeasible(6,U[x],vX ) == True):
                E.append([U[x],vX])
        V.append(vX)
        vL = vX
        print(":",V)

    print("Ilk : ",V)
    V=req.optimization(V)
    print("Son : ",V)




