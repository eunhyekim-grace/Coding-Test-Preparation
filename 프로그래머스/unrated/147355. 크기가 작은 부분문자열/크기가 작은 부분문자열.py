def solution(t, p):
    leng = len(p)
    comp = []
    for i in range(len(t) - leng +1):
        comp.append(t[i:i+leng])
    count = 0
    p_ = int(p)
    for i in range(len(comp)):
        num = int(''.join(comp[i]))
        if num <= p_:
            count+=1
    return count