def solution(wallpaper):
    #get all coordinates of # and get max x,y
    #1 coordinates of # -> x, y separately
    len_y = len(wallpaper)
    len_x = len(wallpaper[0])
    
    idx_x = [i for i in range(len_y) for j in range(len_x) if wallpaper[i][j] == '#']
    idx_y = [j for i in range(len_y) for j in range(len_x) if wallpaper[i][j] == '#']
    
    
    # max x, min x
    min_x, max_x = min(idx_x), max(idx_x)
    #max y, min y
    min_y, max_y = min(idx_y), max(idx_y)
    
    
    answer = [min_x, min_y, max_x+1, max_y+1]
    return answer