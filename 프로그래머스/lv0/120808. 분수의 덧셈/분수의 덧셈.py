def solution(numer1, denom1, numer2, denom2):
    if denom2 % denom1 == 0:
        numer = numer1 * int(denom2 / denom1) + numer2
        denom = denom2
    else:
        numer = numer1 * denom2 + numer2 * denom1
        denom = denom1 * denom2
        
    quo = 1
    till = min(numer, denom) + 1
    #print(numer, denom)
    for i in range(2, till): #최대 공약수 찾기
        if numer % i == 0 and denom % i == 0:
            quo = i
        
    answer = [numer/quo, denom/quo]
    return answer