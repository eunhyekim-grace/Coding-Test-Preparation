def solution(a, b, n):
    count = 0
    while n >= a: #a개 이상의 병이 있을 때 
        count += int(n/a) * b #가진 병에서 a개 당 b개로 받은 수 
        n = int(n%a) + (int(n/a)* b) #n개에서 줄 수 있는 만큼 주고(*a) 다시 돌려받은 병의 수
    
    return count