def mode0(idx):
    if (idx == 0) or (idx % 2 == 0):
        return True
    return False

def mode1(idx):
    if idx % 2 == 1:
        return True
    return False

def solution(code):
    answer = []
    mode = False
    
    for idx, i in enumerate(code):
        if i == '1':
            mode = not mode
        elif mode:
            if mode1(idx):
                answer.append(i)
            else:
                continue
        else:
            if mode0(idx):
                answer.append(i)
    
    if len(answer) == 0:
        return 'EMPTY'
    else:
        answer = ''.join(answer)
        return answer
    return 0