def solution(k, score):
    answer = [score[0]]
    temp = [score[0]] #명예의 전당
    
    for i in range(1, len(score)):
        if len(temp) < k: #크기가 k인 배열 생성
            temp.append(score[i]) #k날 까지는 전부 명예의 전당 in
            answer.append(min(temp)) #명예의 전장에서 제일 작은 수 answer에 append
        else:
            temp.append(score[i]) #k + i날의 점수 명예의 전당 in
            temp.remove(min(temp)) #명예의 전당 update - 제일 낮은 점수 out
            answer.append(min(temp)) #명예의 전당에 있는 제일 작은 점수
            
    return answer