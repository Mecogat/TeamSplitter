def gso(s, p, re):
    team1 = [0] * 4
    team2 = [0] * 4
    teams = [0] * 8
    ii = [0] * 4
    si = 0
    c = 0
    d = 0
    dd = 0
    for i in range(0, 8):
        if(i == re[0] or i == re[1] or i == re[2] or i == re[3]):
            i = i
        else:
            ii[dd] = i
            dd+=1
    for i in range(0, 4):
        if(i < 4):
            team1[i] = re[i]
            team2[i] = ii[i]
    for i in range(0,8):
        if(i < 4):
            teams[i] = team1[i]
        else: 
            teams[i] = team2[i-4]
    return teams
    
