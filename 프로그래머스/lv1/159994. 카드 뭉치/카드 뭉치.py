def solution(cards1, cards2, goal):
    idx = 0
    idx1 = 0
    idx2 = 0
    
    while True:
        if len(goal) == idx:
            answer = 'Yes'
            break
        elif len(cards1) > idx1 and cards1[idx1] == goal[idx]:
            idx += 1
            idx1 += 1
        elif len(cards2) > idx2 and cards2[idx2] == goal[idx]:
            idx += 1
            idx2 += 1
        else:
            answer = 'No'
            break
    #print(idx, idx1, idx2)    
    return answer

