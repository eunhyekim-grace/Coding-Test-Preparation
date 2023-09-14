from collections import Counter

def solution(X, Y):
    both = set(X) & set(Y) #겹치는 수 찾기
    
    if len(both) == 0: #겹치는 수 X
        return '-1'
    elif list(both)[0] == '0' and len(both) == 1: #겹치는 수가 0 밖에 없을 때
        # print('t')
        return '0'
    else:
        xc = Counter(X)
        yc = Counter(Y)
        pos = []
        for i in list(both): #겹치는 수만 
            #print(int(counter.get(i)/2))
            count = min([xc.get(i), yc.get(i)]) #양쪽에 다 있는 수 만큼 
            tmp = [i] * count
            pos = pos +tmp #list에 추가
        #print(pos)
        answer = ''.join(sorted(pos, reverse = True)) #내림차순 정렬해서 문자열로 return
        #print(answer)
    return answer