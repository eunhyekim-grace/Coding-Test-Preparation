
def move(direc, num, sr, sc, r_max, c_max, sep_park):
    if direc == 'E':
        # print('E ', sr, sc, c_max)
        if sc + num >= c_max:
            return sr, sc
        else:
            mc = sc
            for i in range(num):
                mc += 1
                if sep_park[sr][mc] == 'X':
                    return sr, sc
                # else:
                    # mc += 1
        return sr, mc
    elif direc == 'W':
        if sc - num < 0:
            return sr, sc
        else:
            mc = sc
            for i in range(num):
                mc -= 1
                if sep_park[sr][mc] == 'X':
                    return sr, sc
                # else:
                    # mc -= 1
        return sr, mc
        
    elif direc == 'S':
        if sr + num >= r_max:
            return sr, sc
        else:
            mr = sr
            for i in range(num):
                mr += 1
                if sep_park[mr][sc] == 'X':
                    return sr, sc
                # else:
                    # mr += 1
        return mr, sc
    else:
        if sr - num < 0:
            return sr, sc
        else:
            mr = sr
            for i in range(num):
                mr -= 1
                if sep_park[mr][sc] == 'X':
                    return sr, sc
                # else:
                    # mr -= 1
        return mr, sc
#         return [current[0]-1, current[1]]

    return sr, sc
    
def solution(park, routes):
    #save park -> 2D array
    sep_park= [[i[j] for j in range(len(i))] for i in park]
    # print(sep_park)
    r_max = len(sep_park) 
    c_max = len(sep_park[0]) 
    
    #find start point
    start = [(i,j) for i in range(r_max) for j in range(c_max) if sep_park[i][j] == 'S']
    sr = start[0][0]
    sc = start[0][1]
    
    
    for char in routes:
        direc, num = char[0], int(char[2])
        # print(direc, type(num))
        sr, sc = move(direc, num, sr, sc, r_max, c_max, sep_park)
        # print(sr, sc)
    
    return [sr, sc]