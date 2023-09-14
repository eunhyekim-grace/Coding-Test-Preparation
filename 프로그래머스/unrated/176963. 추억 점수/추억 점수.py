def solution(name, yearning, photo):
    score_dict = {}
    for n, num in zip(name, yearning):
        score_dict[n] = num
    
    answer = []
    for line in photo:
        score = 0
        for name in line:
            if name in score_dict.keys():
                 score += score_dict[name]
            else:
                continue
        answer.append(score)
    return answer