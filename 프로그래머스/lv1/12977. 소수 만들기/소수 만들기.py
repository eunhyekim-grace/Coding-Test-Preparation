from itertools import combinations 

def check_prime(num): #소수 판별
    for i in range(2,num): 
        if num % i == 0:
            return 0
    return 1

def solution(nums):
    answer = 0
    possible = list(combinations(nums, 3)) #가능한 3자리수 조합 모두 return
    for i in possible:
        num = sum(i)
        answer += check_prime(num)

    return answer