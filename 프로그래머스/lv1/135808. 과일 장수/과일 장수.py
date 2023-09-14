def solution(k, m, score):
    sorted_score = sorted(score)[::-1] #점수가 제일 높은 값부터 정렬
    impossible = int((len(score))%m) #상자 안에 들어가지 못하는 나머지 과일의 수
    answer = 0
    for i in range(0,len(score)-impossible,m): #과일 상자에 들어갈 수 있는 수까지 m개 씩
        answer += (min(sorted_score[i:i+m]) * m) #해당 과일 상자의 가장 낮은 점수 * m
    return answer