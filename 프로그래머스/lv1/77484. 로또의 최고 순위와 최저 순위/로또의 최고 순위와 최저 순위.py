def solution(lottos, win_nums):
    score_dict = {idx+1 : val for idx,val in enumerate(range(6, 0, -1))}
    score_dict[0] = 6 # lotto의 점수 dict 생성
    
    if 0 not in lottos: #0이 하나도 없는 경우
        cnt = [i for i in lottos if i in win_nums]
        score = score_dict.get(len(cnt))
        answer = [score, score] #현재 같은 수 만큼이 최고, 최저 등수
    else:
        cnt = [i for i in lottos if i in win_nums]
        zeros = [i for i in lottos if i == 0]
        
        score = score_dict.get(len(cnt))
        if len(zeros) == 6: #전부 다 0인 경우 
            answer = [1, 6] #최고 1등, 최저 6등
        else:
            answer = [score - len(zeros), score] #최저는 현재 같은 수 만큼, 최고는 최저 + 0의 개수

    return answer