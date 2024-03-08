def solution(n,a,b):
    answer = 0
    #a,b가 붙게되는 라운드 구하기
    
    #logic -> 짝수: n /2 , 홀수: (n+1) / 2
    #a의 다음 라운드 - 4/2 = 2, b의 다음 라운드 - 8/2 = 4 => 1
    #a의 다음 라운드 - 2/2 = 1, b의 다음 라운드 - 4/2 = 2 => 2
    #a의 다음 라운드 - 2/2 = 1, b의 다음 라운드 - 2/2 = 1 => 3
    #여기서 만남
    
    #첫 라운드에 만날 경우
    a_next = a / 2 if a % 2 == 0 else (a+1) / 2
    b_next = b / 2 if b % 2 == 0 else (b+1) / 2
    if a_next == b_next:
        return 1
    else:
        n_round = 1
        while a_next != b_next:
            a_next = a_next / 2 if a_next % 2 == 0 else (a_next+1) / 2
            b_next = b_next / 2 if b_next % 2 == 0 else (b_next+1) / 2
            n_round += 1
    
        return n_round
    return answer