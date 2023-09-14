from collections import Counter

def solution(participant, completion):
    answer = list(set(participant) ^ set(completion))
    if len(answer) == 0:
        part = Counter(participant)
        comp = Counter(completion)
        
        diff = set(dict(comp).items()) ^ set(dict(part).items())
        return str(list(dict(diff).keys())[0])
    else:
        return answer[0]
