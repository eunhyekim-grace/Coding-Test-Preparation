def solution(common):
    diff1 = common[1] - common[0] #두 번째 원소와 첫 번째 원소 간의 차
    diff2 = common[2] - common[1] #세 번째 원소와 두 번째 원소 간의 차
    if diff1 == diff2:
        answer = common[-1] + diff1
        return answer
    else:
        diff = int(common[2] / common[1])
        leng = len(common)
        answer = common[0] * (diff **leng)
        return answer
    answer = 0
    return answer