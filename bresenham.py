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
