def solution(n):
    
    cnt = 1 #자기 자신
    for i in range(1,n//2 +1):
        temp = 0
        # print(i)
        for j in range(i, n//2+3):
            # print(i,j)
            if temp > n:
                break
            elif temp == n:
                # print(i,j)
                cnt += 1
            temp += j
    
    # print(cnt)
    # answer = 0
    return cnt