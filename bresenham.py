import numpy as np

def bresenham(x0,y0,x1,y1):
    c = []
    dx = abs(x1-x0)
    dy = abs(y1-y0)
    x = x0
    y = y0
    ii = 0
    n = dx + dy
    err = dx - dy
    x_inc = 1
    y_inc = 1

    max_length = (max(dx,dy)+1)*3

    rr = np.zeros( max_length, dtype = np.intp )
    cc = np.zeros( max_length, dtype = np.intp )

    if x1 > x0: x_inc = 1
    else:       x_inc = -1
    if y1 > y0: y_inc = 1
    else:       y_inc = -1

    dx = 2 * dx
    dy = 2 * dy

    while n > 0:
        c.append([x,y])
        rr[ii] = y
        cc[ii] = x
        ii = ii + 1
        if (err > 0):
            x += x_inc
            err -= dy
        elif (err < 0):
            y += y_inc
            err += dx
        else:  # If err == 0 the algorithm is on a corner
            rr[ii] = y + y_inc
            cc[ii] = x
            rr[ii + 1] = y
            cc[ii + 1] = x + x_inc
            ii = ii + 2
            x += x_inc
            y += y_inc
            err = err + dx - dy
            n = n - 1
        n = n - 1
    c.append( [x, y] )
    rr[ii] = y
    cc[ii] = x
    return c






"""

def bresenham(x0, y0, x1, y1):

    c = [[]]
    c.pop() #Buraya bir bak
    temp = 0
    dX = abs(x1 - x0)
    dY = abs(y1 - y0)
    error =  2 * dY - dX
    x = x0
    y = y0

    while x<x1+1:
        c.append( [x, y] )
        x +=1

        if error>=0:
            if (temp != 1 and y+1 <= y1):
                c.append([x,y])

            else:
                temp =0

            y+=1
            error += (2 * dY - 2*dX)
        else:
            if (y + 1 <= y1):
                c.append([x,y+1])

            temp = 1
            error += 2*dY

    return c







    x= x0 - x1
    y= y0 - y1
    dX = 2* abs(x0 - x1)
    dY = 2* abs(y0 - y1)

    c = [[]]
    c.pop()  # Buraya bir bak

    if dX > dY:
        sigma=(dY-dX)/2
        error = 0
        tempx,tempy = x1,y1
        while tempx!=x0:
            c.append( [tempx, tempy] )
            print(tempx)
            if error>sigma:
                tempx+=x
                error -= dY
            elif error < sigma:
                tempy += y
            else:
                tempx += x
                tempy += y
                error += (dX-dY)
                
"""