def solution(n,m,section):
    if m == 1:
        return int(len(section) / m)
    else:
        left = section
        result = 0
        while left:
            end = left[0] +m -1
            result += 1
            left = [i for i in left if i> end]
    
            
    return result
# 3개 시간초과