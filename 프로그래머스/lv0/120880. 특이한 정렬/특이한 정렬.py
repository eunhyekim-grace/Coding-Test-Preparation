from itertools import chain

def solution(numlist, n):
    dist= {}
    for i in numlist:
        diff = abs(n - i)
        if diff in dist:
            dist[diff].append(i)
        else:
            dist[diff] = [i]
        
    
    dist = dict(sorted(dist.items()))
    answer = []
    for k,v in dist.items():
        #print(v)
        answer.append(sorted(v, reverse= True))
    
    answer = list(chain(*answer))
    #print(answer)
    return answer