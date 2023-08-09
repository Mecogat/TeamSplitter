import bck
def FNN(s, p):
    ss = [0] * 28
    re = [0] * 4
    xx = [""] * 28
    yy = [""] * 28
    hi = 0
    de = 0
    order1 = [0] * 28
    order2 = [0] * 28
    for i in range(0, 7):
        for ii in range(0,(7-i)):
            xx[de] = p[i]
            yy[de] = p[ii+i+1]
            de+=1
    de = 0
    for i in range(0, 7):
        for ii in range(0,(7-i)):
            order1[de] = i
            order2[de] = ii+i+1
            de+=1
    check = bck.booleancheck(xx, yy)
    for y in range (0,8):
        for x in range(y, 8):
            if(p[y] == p[x]):
                de = 0
            else:
                ss[hi] = s[y] + s[x]
                hi+=1
    pairs = []
    for y in range(0,28):
        for x in range(0,28):
            if(check[x][y] == True):
                if(ss[x] + ss[y] == 0):
                    buf = [order1[x], order2[x], order1[y], order2[y]]
                    pairs.append(buf)
    return pairs
