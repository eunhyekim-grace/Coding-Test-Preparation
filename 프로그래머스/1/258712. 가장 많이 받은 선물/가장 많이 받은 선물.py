def solution(friends, gifts):
    # dict indicates the interaction between friends
    #{muzi: {ryan:0, frodo: 0, neo:0}, ...}
    interactions = {i: {j: 0 for j in friends} for i in friends}
    # dict for present_score
    present_score = {i : 0 for i in friends}
    # dict for the next month present count
    present_r = {i:0 for i in friends}
    
    #calculate interactions and present score
    for i in gifts:
        a, b = i.split(' ')
        interactions.get(a)[b] += 1
        #if someone gives present + 1, receives present - 1
        present_score[a] += 1
        present_score[b] -= 1
    
    #calculate the number of presents of each friends will receive next month
    for i in range(len(friends)-1):
        for j in range(i+1, len(friends)):
            a = friends[i]
            b = friends[j]
            ab = interactions.get(a)[b]
            ba = interactions.get(b)[a]
            if (ab != ba) and ((ab != 0) or (ba != 0)):
                friend = a if ab > ba else b
                present_r[friend] += 1
            elif ab == ba:
                if present_score.get(a) != present_score.get(b):
                    friend = a if present_score.get(a) > present_score.get(b) else b
                    present_r[friend] +=1
                
        
    
    # answer = 0
    answer = sorted(present_r.items(), key = lambda x: x[1], reverse = True)[0][1]
    return answer

'''
 case1: record 0 / count diff - less -> more
 case2: record X / count same - cal present_score / ps low -> large
    present_score = give - receive
    case3: present_score same - X
 output: # of present of the one who received the most next month
 input:
    friends = name of friends / list
    gifts = present log / list
'''