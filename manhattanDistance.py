import math
def ManhattanDistance(array):
    #Our array's dimensions
    M=6
    N=6
    totalDistance = 0

    for x in range(0,len(array)):

        Xfirst = math.ceil(array[x]/6)  # X coordinate of our first point
        Yfirst = array[x] % 6   # Y coordinate of our first point

        if(len(array) != x+1):
            Xsecond = math.ceil(array[x+1]/6)
            Ysecond = array[x+1] % 6
        else:
            Xsecond = 6
            Ysecond = 6


        # If remainder is 0 we have to change it to 6
        if Yfirst == 0:
            Yfirst = 6

        if Ysecond == 0:
            Ysecond = 6

        distance = math.fabs(Xsecond - Xfirst) + math.fabs(Ysecond - Yfirst)
        totalDistance = distance+totalDistance

    print("Total: ",totalDistance)