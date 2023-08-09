def booleancheck(xx, yy):
    check = [[False for i in range(28)] for ii in range(28)]
    for y in range(0,28):
        for x in range (0, 28):
            if(xx[x] == yy[y] or xx[y] == yy[x] or xx[x] == xx[y] or yy[x] == yy[y]):
                check[x][y] = False
            else:
                check[x][y] = True
    return check
