def scoreupdt(s, wt, ss):
    if(wt == 1):
        for i in range(0,4):
            s[ss[i]] = (s[ss[i]]) + 1
        for i in range(4,8):
            s[ss[i]] = (s[ss[i]]) - 1
    else:
        for i in range(0,4):
            s[ss[i]] = (s[ss[i]]) - 1
        for i in range(4,8):
            s[ss[i]] = (s[ss[i]]) + 1
    return s
