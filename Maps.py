import random 
def Randommap(count):
    sz = ['Hagglefish Market', 'Museum d\'Alfonsino', 'Mahi-Mahi Resort', 'Inkblot Art Academy', 'Sturgeon Shipyard', 'MakoMart', 'Um\'ami Ruins', 'Humpback Pump Track', 'Barnacle & Dime']
    szz = sz
    tc = ['Hagglefish Market', 'Undertow Spillway', 'Museum d\'Alfonsino', 'Inkblot Art Academy', 'Sturgeon Shipyard', 'MakoMart', 'Manta Maria', 'Humpback Pump Track', 'Barnacle & Dime']
    tcc = tc
    rm = ['Scorch Gorge', 'Eeltail Alley', 'Hagglefish Market', 'Undertow Spillway', 'Museum d\'Alfonsino','Sturgeon Shipyard', 'Humpback Pump Track', 'Barnacle & Dime']
    rmm = rm
    cb = ['Scorch Gorge', 'Hagglefish Market', 'Museum d\'Alfonsino', 'Inkblot Art Academy', 'MakoMart', 'Manta Maria', 'Humpback Pump Track', 'Barnacle & Dime']
    cbb = cb
    counts = float(count)/4
    mode = (counts - int(counts)) * 4
    mapbuf1 = ''
    mapbuf2 = ''
    mapbuf3 = ''
    bufcount = 0
    fmap = ""
    if count == 1:
        fmap = ("map is sz MakoMart")
        sz[5] = 'no repeat'
        mode = 2
    else:
        if mode == 1:
            map = random.randint(0,8)
            while mapbuf1 == sz[map] or mapbuf2 == sz[map] or mapbuf3 == sz[map] or sz[map] == 'no repeat':
                map = random.randint(0,8)
                bufcount = bufcount + 1
                if  bufcount < 7:
                    sz = szz
            fmap = ("map is sz " + str(sz[map]))
            mapbuf3 = mapbuf2
            mapbuf2 = mapbuf1
            mapbuf1 = sz[map]
            sz[map] = 'no repeat'
            mode = mode + 1
            bufcount = 0
        elif mode == 2:
            map = random.randint(0,8)
            while mapbuf1 == tc[map] or mapbuf2 == tc[map] or mapbuf3 == tc[map] or tc[map] == 'no repeat':
                map = random.randint(0,8)
                bufcount = bufcount + 1
                if  bufcount < 7:
                    tc = tcc
            fmap = ("map is tc " + str(tc[map]))
            mapbuf3 = mapbuf2
            mapbuf2 = mapbuf1
            mapbuf1 = tc[map]
            tc[map] = 'no repeat'
            mode = mode + 1
            bufcount = 0
        elif mode == 3:
            map = random.randint(0,7)
            while mapbuf1 == rm[map] or mapbuf2 == rm[map] or mapbuf3 == rm[map] or rm[map] == 'no repeat':
                map = random.randint(0,7)
                bufcount = bufcount + 1
                if  bufcount < 7:
                    rm = rmm
            fmap = ("map is rm " + str(rm[map]))
            mapbuf3 = mapbuf2
            mapbuf2 = mapbuf1
            mapbuf1 = rm[map]
            rm[map] = 'no repeat'
            mode = mode + 1
            bufcount = 0
        elif mode == 0:
            map = random.randint(0,7)
            while mapbuf1 == cb[map] or mapbuf2 == cb[map] or mapbuf3 == cb[map] or cb[map] == 'no repeat':
                map = random.randint(0,7)
                bufcount = bufcount + 1
                if  bufcount < 7:
                    cb = cbb
            fmap = ("map is cb " + str(cb[map]))
            mapbuf3 = mapbuf2
            mapbuf2 = mapbuf1
            mapbuf1 = cb[map]
            cb[map] = 'no repeat'
            mode = 1
            bufcount = 0
    return fmap
