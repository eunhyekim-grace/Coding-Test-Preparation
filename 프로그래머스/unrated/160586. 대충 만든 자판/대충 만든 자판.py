def solution(keymap, targets):
    key_dict = {}
    for i in keymap: #keymap에 있는 alphabet의 key 최소 횟수를 dict에 저장
        for idx, key in enumerate(i):
            if key in key_dict:
                key_dict[key] = idx+1 if key_dict[key] > idx+1 else key_dict[key]
            else:
                key_dict[key] = idx+1
    
    answer = []

    for i in targets:
        temp = [key_dict.get(target) if target in key_dict else -1 for target in i]
        if -1 in temp: #target을 완성할 수 없는 경우
            answer.append(-1)
        else: #target을 위한 횟수의 합
            answer.append(sum(temp))
    return answer