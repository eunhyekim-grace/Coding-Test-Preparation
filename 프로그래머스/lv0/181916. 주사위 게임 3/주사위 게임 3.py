from collections import Counter

def solution(a, b, c, d):
    s = set([a,b,c,d])
    answer = 0
    #print(s)
    if len(s) == 1:
        answer = 1111 * list(s)[0]
    elif len(s) == 4:
        answer = min(list(s))
    else:
        counter = Counter([a,b,c,d])
        if len(counter) == 3:
            temp = counter.most_common(3)
            q, r = temp[1][0], temp[2][0]
            answer = q*r
        else:
            temp = counter.most_common(2)
            if temp[0][1] == 3:
                p, q = temp[0][0], temp[1][0]
                answer = (10 * p + q) ** 2
            else:
                p, q = temp[0][0], temp [1][0]
                answer = (p+q) * abs(p - q)
    return answer