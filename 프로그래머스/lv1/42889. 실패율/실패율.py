from collections import Counter

def solution(N, stages):
    counter = Counter()
    for i in stages: # 현재 player들이 있는 stage counter사용해서 dict에 저장
        counter[i] += 1

    total = len(stages)
    t = sorted(counter.items(), key = lambda pair: pair[0]) #stage 1~ N+1까지 순서대로 정렬

    cal = {}
    for i in t: #각 stage의 실패율을 계산해서 cal이라는 dict에 저장
        key, val = i
        cal[key] = val/total
        total -= val
        
    t_ = sorted(cal.items(), key = lambda pair: pair[1], reverse = True) #실패율이 높은 것부터 정렬

    answer = [i[0] for i in t_] #dict의 stage만 answer에 저장

    if N+1 in answer: #N+1이 있는 경우 삭제
        answer.remove(N+1)
    for i in range(1, N+1): #answer에 없는 경우 실패율을 0으로 간주하고 순서대로 answer에 append
        if i not in answer:
            answer.append(i)

    return answer