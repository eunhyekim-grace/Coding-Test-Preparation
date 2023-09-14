def solution(n, lost, reserve):
    #answer = n - len(lost)
    #ascending / descending 둘 중 하나로만 greedy 
    
    #2 way -> for loop 많이 vs search 많이
    
#     lost_ = sorted(lost)
#     reserve_ = sorted(reserve)
#     for i in reserve_:
#         print(i)
#         if i-1 in lost_:
#             lost_.remove(i-1)
#             reserve.remove(i)
    
#     if not(reserve) and not(lost):
#         reserve_ = reserve
#         for i in reserve_:
#             if i+1 in lost:
#                 lost_.remove(i+1)
#                 reserve.remove(i)
    
#     answer = n - len(lost_)
                    
    # print(lost_, reserve_)
    
    r_lost = set(reserve) & set(lost)
    reserve = list(set(reserve) ^ r_lost)
    lost = list(set(lost) ^ r_lost)
    
    for i in reserve:
        if i - 1 in lost:
            lost.remove(i-1)
        elif i + 1 in lost:
            lost.remove(i+1)

    answer = n - len(lost)
    return answer

#5개 실패